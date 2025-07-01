# 🛰️ SmartBeam: Real-Time Object Tracking & Projection System

📘 [English](README.md) | 🇰🇷 [한국어](README.ko.md)

SmartBeam is a real-time object tracking pipeline using YOLOv11 instance segmentation in Python, designed to send object coordinates (e.g., plate, bowl, clock) to Unity via WebSocket. Unity then uses these coordinates to align a projected animation or video, creating a seamless projection mapping effect similar to *Le Petit Chef*.

---

## 🏢 About

SmartBeam is developed and maintained by **CSI Vision**, a company focused on real-time spatial computing, projection mapping, and computer vision solutions.

For inquiries or collaboration opportunities, contact us at [js.lee@csi-vision.com](mailto:js.lee@csi-vision.com).

---

## 📁 Project Structure
```
.
├── config.py
├── detector.py
├── logger.py
├── main.py
├── utils.py
└── websocket_server.py
```
---

## 🔧 File Descriptions

### `main.py`
**Main entry point** of the system.  
- Starts the WebSocket server and detection loop in parallel using threading.
- Coordinates all components of the system.

### `config.py`
**Configuration file** defining system constants.  
- `ALLOWED_CLASSES`: COCO classes like "bowl", "clock", etc.
- `MODEL_PATH`: Path to YOLOv11 segmentation model.
- `CAMERA_ID`: OpenCV-compatible camera index.

### `detector.py`
**YOLOv11-based object detection module**.  
- Captures frames via OpenCV.
- Runs YOLOv11 segmentation.
- Extracts centroid from segmentation masks.
- Sends coordinates to a shared queue for Unity.

### `websocket_server.py`
**WebSocket server** using `websockets` and `asyncio`.  
- Listens for Unity client connection.
- Sends real-time coordinates via WebSocket.

### `utils.py`
**Helper functions**:
- Centroid calculation from binary masks.
- Visualization for debugging.

### `logger.py`
**Minimal logging utility**.
- Provides standardized log messages.

---

## 🔁 Workflow Summary

1. **Python Side**:
   - YOLOv11 performs segmentation on webcam input.
   - Calculates centroid of objects.
   - Sends object position via WebSocket.

2. **Unity Side**:
   - Receives coordinates from Python.
   - Updates a projected video to match the object's position.

---

## 🧠 Use Cases

SmartBeam is ideal for:
- Restaurants with interactive projection tables.
- Augmented reality experiences with physical props.
- Projection mapping demos needing high precision.

---

## 🔌 Requirements

- Python 3.9+
- OpenCV
- `ultralytics` (YOLOv11 support)
- `websockets`
- Unity project with WebSocket receiver

---

## 📦 Download YOLOv11 Model

You will need the YOLOv11 instance segmentation model to run this project.

1. Download the pretrained model:  
   [**yolo11n-seg.pt**](https://docs.ultralytics.com/ko/tasks/segment/)  
   *(Or use your own trained `.pt` model if preferred)*

2. Place the model file in your project root or update `MODEL_PATH` in `config.py` accordingly:
```python
MODEL_PATH = "yolo11n-seg.pt"
```

---

## 🚀 Run Instructions
```bash
pip install -r requirements.txt
python main.py
```
Make sure your Unity scene is open and listening for WebSocket data to receive the real-time coordinates.
