# Dhan Option Chain WebSocket Backend

## Overview

A FastAPI backend service that connects to Dhan's WebSocket API and relays real-time option chain and spot price updates to your frontend clients.

---

## Features

- WebSocket relay from Dhan API to unlimited frontend clients
- Dockerized and easy to deploy
- CORS enabled for any frontend
- Ready for extension with analytics, signal logic, and more

---

## Setup

### 1. Clone and Configure

```bash
git clone https://github.com/saikumarraju5/dhan-option-backend.git
cd dhan-option-backend
cp .env.example .env
# Edit .env and fill in your Dhan API credentials
```

### 2. Run Locally

```bash
pip install -r requirements.txt
python dhan_ws_bridge.py
```

### 3. Run with Docker

```bash
docker-compose up --build
```

The backend will be available at `ws://localhost:8000/ws`

---

## WebSocket Usage

- Connect your frontend WebSocket client to: `ws://<your-server>:8000/ws`
- You will receive real-time messages from Dhan

---

## Environment Variables (`.env`)

- `DHAN_ACCESS_TOKEN`: Your Dhan API WebSocket token
- `DHAN_WS_URL`: Dhan WebSocket endpoint
- `DHAN_INSTRUMENT`: Option chain instrument (default: NSE_INDEX|SENSEX)
- `DHAN_MODE`: Subscription mode (default: full)

---

## Extending

Add your own logic inside `dhan_ws_bridge.py` for event parsing, analytics, or trading.

---

## License

MIT