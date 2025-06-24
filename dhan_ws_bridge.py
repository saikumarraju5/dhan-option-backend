import asyncio
import os
import websockets
import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

load_dotenv(".env")

DHAN_WS_URL = os.getenv("DHAN_WS_URL", "wss://api.dhan.co/option-chain/stream")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")
INSTRUMENT = os.getenv("DHAN_INSTRUMENT", "NSE_INDEX|SENSEX")
MODE = os.getenv("DHAN_MODE", "full")

app = FastAPI()

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)

async def dhan_ws_consumer():
    async with websockets.connect(
        DHAN_WS_URL, 
        extra_headers={"access-token": DHAN_ACCESS_TOKEN}
    ) as ws:
        await ws.send(json.dumps({
            "instrument": INSTRUMENT,
            "mode": MODE
        }))

        while True:
            message = await ws.recv()
            print(f"Received: {message}")
            # Relay to all connected clients
            for client in clients:
                try:
                    await client.send_text(message)
                except:
                    clients.remove(client)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(dhan_ws_consumer())
    uvicorn.run(app, host="0.0.0.0", port=8000)