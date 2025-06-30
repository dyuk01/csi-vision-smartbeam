import asyncio
import json
import threading

import websockets

from config import WEBSOCKET_PORT
from logger import log_event

packet_queue = None

async def echo(websocket) -> None:
    log_event("✅ Unity client connected.")
    try:
        while True:
            await asyncio.sleep(0.01)
            while not packet_queue.empty():
                packet = packet_queue.get()
                try:
                    await websocket.send(json.dumps(packet))
                except Exception as e:
                    log_event(f"❌ Error sending packet: {str(e)}")
    except websockets.exceptions.ConnectionClosed:
        log_event("🔌 Unity disconnected.")
    except Exception as e:
        log_event(f"❌ WebSocket error: {str(e)}")


async def websocket_main() -> None:
    log_event(f"🌐 WebSocket server initialized on ws://localhost:{WEBSOCKET_PORT}")
    async with websockets.serve(echo, "localhost", WEBSOCKET_PORT):
        await asyncio.Future()


# Start the WebSocket server in a separate thread
def start_server(queue) -> None:
    log_event("🌐 Starting WebSocket server...")
    global packet_queue
    packet_queue = queue

    # Run the WebSocket server in a separate thread
    def start_thread() -> None:
        try:
            asyncio.run(websocket_main())
        except Exception as e:
            log_event(f"❌ Server init failed: {str(e)}")

    threading.Thread(thread=start_thread(), daemon=True).start()
