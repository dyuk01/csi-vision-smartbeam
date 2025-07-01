import asyncio
import json
import threading
import queue
from typing import Any

import websockets
from websockets.legacy.server import WebSocketServerProtocol

from config import WEBSOCKET_PORT
from logger import log_event

packet_queue: queue.Queue[dict[str, Any]] | None = None

def start_server(queue_: queue.Queue[dict[str, Any]]) -> None:
    log_event("🌐 Starting WebSocket server...")

    async def echo(websocket: WebSocketServerProtocol) -> None:
        log_event("✅ Unity client connected.")
        try:
            while True:
                await asyncio.sleep(0.01)
                while not queue_.empty():
                    packet = queue_.get()
                    try:
                        await websocket.send(json.dumps(packet))
                    except Exception as e:
                        log_event(f"❌ Error sending packet: {e}")
        except websockets.exceptions.ConnectionClosed:
            log_event("🔌 Unity disconnected.")
        except Exception as e:
            log_event(f"❌ WebSocket error: {e}")

    async def websocket_main() -> None:
        log_event(f"🌐 WebSocket server on ws://localhost:{WEBSOCKET_PORT}")
        async with websockets.serve(echo, "localhost", WEBSOCKET_PORT):
            await asyncio.Future()

    def start_thread() -> None:
        try:
            asyncio.run(websocket_main())
        except Exception as e:
            log_event(f"❌ Server init failed: {e}")

    threading.Thread(target=start_thread, daemon=True).start()
