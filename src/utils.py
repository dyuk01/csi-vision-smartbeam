import cv2
import numpy as np

def singular(word: str) -> str:
    return word.lower().rstrip("s")


def calculate_centroid_from_mask(mask: np.ndarray) -> tuple[int, int] | None:
    moments = cv2.moments(mask.astype(np.uint8))
    if moments["m00"] != 0:
        x = int(moments["m10"] / moments["m00"])
        y = int(moments["m01"] / moments["m00"])
        return (x, y)
    return None


def draw_centroid_and_info(frame, centroid, class_name, confidence, color=(0, 255, 0)) -> None:
    if centroid is not None:
        x, y = centroid
        cv2.circle(frame, (x, y), 6, color, -1)
        cv2.circle(frame, (x, y), 8, (255, 255, 255), 2)
        cv2.line(frame, (x - 15, y), (x + 15, y), color, 2)
        cv2.line(frame, (x, y - 15), (x, y + 15), color, 2)
        text = f"{class_name}: ({x}, {y}) conf:{confidence:.2f}"
        cv2.putText(frame, text, (x - 50, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(frame, text, (x - 50, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

