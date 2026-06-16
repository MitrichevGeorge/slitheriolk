from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from ..world import World

app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>LK slither.io srv</title>
    </head>
    <body>
        <h1> This server is for api only </h1>
    </body>
</html>
"""

now_pid = -1

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.get("/pid", response_model=int)
async def get_pid():
    global now_pid
    now_pid += 1
    return now_pid

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        pid = int(await websocket.receive_text())
        if pid > now_pid:
            await websocket.send_text("Unreal player")
            await websocket.close()
            return
        while True:
            pass
    except WebSocketDisconnect:
        print("Client disconnected")
