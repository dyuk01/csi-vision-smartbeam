from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Change the directory depending on your YOLO model location.

# === Model Settings ===
MODEL_PATH = BASE_DIR / "yolo11n-seg.pt"
ALLOWED_CLASSES = {"cup", "bowl", "plate", "table", "dining table"}

# === Video Input Settings ===
CAMERA_ID = 0
VIDEO_SOURCE = 0
SHOW_PREVIEW = True

# === WebSocket Settings ===
WEBSOCKET_PORT = 50000
