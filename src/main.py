import queue

from detector import Detector
from logger import log_event
from websocket_server import start_server

log_event("🚀 Program started.")

# Initialize shared queue
packet_queue = queue.Queue()

# Start WebSocket server
start_server(packet_queue)

# Run detection loop
detector = Detector(packet_queue)
detector.run()

log_event(f"✅ Program terminated.\n")