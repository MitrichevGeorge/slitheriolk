from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

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

class World:
    def __init__(self):
        px = []
        py = []

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
        peer = crypt_ws.Communicator_server(websocket, k_sign_priv)
        await peer.exchange()
        await peer.send(b"hello everyone!")
        print(await peer.recv_str())
        print(await peer.recv_str())
        print(await peer.recv_str())
    except WebSocketDisconnect:
        print("Client disconnected")