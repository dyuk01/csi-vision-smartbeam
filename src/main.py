import queue

from detector import Detector
from logger import log_event
from websocket_server import start_server

def main() -> None:
    # Starting program message
    log_event("")
    log_event(f"🚀 Program started.")

    # Initialize the WebSocket server and detector
    packet_queue = queue.Queue()
    start_server(packet_queue)
    detector = Detector(packet_queue)
    detector.run()

    log_event(f"✅ Program terminated.")


if __name__ == "__main__":
    main()