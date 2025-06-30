import time
import cv2
import numpy as np
from ultralytics import YOLO

from config import ALLOWED_CLASSES, CAMERA_ID, MODEL_PATH
from logger import log_event
from utils import calculate_centroid_from_mask, draw_centroid_and_info, singular


class Detector:
    def __init__(self, packet_queue):
        log_event("🔍 Initializing detector...")
        self.packet_queue = packet_queue
        self.model = YOLO(MODEL_PATH)
        log_event(f"📦 Loaded model from {MODEL_PATH}")
        self.cap = cv2.VideoCapture(CAMERA_ID)
        log_event(f"📷 Opened camera {CAMERA_ID}")

    def run(self):
        log_event("🔍 Starting detection loop...")
        if not self.cap.isOpened():
            print(f"❌ Failed to open camera {CAMERA_ID}")
            return

        while True:
            success, frame = self.cap.read()
            if not success:
                print("⚠️ Failed to read from webcam.")
                break

            start = time.perf_counter()
            results = self.model(frame)
            end = time.perf_counter()
            fps = 1 / (end - start)
            annotated_frame = frame.copy()

            for result in results:
                if result.masks is None:
                    continue

                masks = result.masks.data.cpu().numpy()
                classes = result.boxes.cls.cpu().numpy()
                confidences = result.boxes.conf.cpu().numpy()
                class_names = [self.model.names[int(cls)] for cls in classes]

                objects = []

                for i in range(len(masks)):
                    mask = cv2.resize(masks[i], (frame.shape[1], frame.shape[0]))
                    centroid = calculate_centroid_from_mask(mask)

                    color = (
                        int(classes[i] * 50) % 255,
                        int(classes[i] * 100) % 255,
                        int(classes[i] * 150) % 255
                    )

                    mask_colored = np.zeros_like(frame)
                    mask_colored[mask > 0.5] = color
                    annotated_frame = cv2.addWeighted(annotated_frame, 1.0, mask_colored, 0.3, 0)

                    contours, _ = cv2.findContours((mask > 0.5).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cv2.drawContours(annotated_frame, contours, -1, color, 2)

                    draw_centroid_and_info(annotated_frame, centroid, class_names[i], confidences[i], color)

                    if centroid and class_names[i] in ALLOWED_CLASSES:
                        singular_class = singular(class_names[i])
                        objects.append({
                            "x": centroid[0],
                            "y": centroid[1],
                            "class_id": singular_class,
                            "confidence": float(confidences[i])
                        })

                if objects:
                    self.packet_queue.put({ "objects": objects })
                    # log_event(f"📦 Sent {len(objects)} object(s)")

            cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("SmartBeam Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
