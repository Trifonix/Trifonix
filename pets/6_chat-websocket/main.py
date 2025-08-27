from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

clients = {}
messages = []

colors = ["red", "blue", "green", "purple", "orange", "brown", "teal", "magenta"]

@app.websocket("/ws/{nickname}")
async def websocket_endpoint(websocket: WebSocket, nickname: str):
    await websocket.accept()
    
    used_colors = [info["color"] for info in clients.values()]
    available_colors = [c for c in colors if c not in used_colors]
    color = available_colors[0] if available_colors else "black"
    
    clients[websocket] = {"nickname": nickname, "color": color}
    
    for msg, nick, c in messages:
        await websocket.send_text(f'<span style="color:{c}">{nick}: {msg}</span>')
    
    try:
        while True:
            data = await websocket.receive_text()
            messages.append((data, nickname, color))
            for client in clients:
                await client.send_text(f'<span style="color:{color}">{nickname}: {data}</span>')
    except WebSocketDisconnect:
        del clients[websocket]
        print(f"{nickname} отключился")
