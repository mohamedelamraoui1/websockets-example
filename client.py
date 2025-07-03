import asyncio
import websockets

async def hello():
    url="ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        name=input("Enter your name: ")
        await websocket.send(name)
        print(f"Sent: {name}")
        greeting = await websocket.recv()
        print(f"Received: {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())