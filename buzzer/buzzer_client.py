import asyncio
import websockets   
import keyboard

# start th websocket client 
async def start_client():
    # Connect to the WebSocket server running on localhost port 8765
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Set up a flag to control the main loop
        done=False
        # Keep the client running until we're done
        while not done:
            # Check if the spacebar is currently being pressed
            if keyboard.is_pressed('space'):
                await websocket.send("buzz")
                message = await websocket.recv()
                print(f"Received: {message}")
                # Set done to True to exit the loop after one buzz
                done = True

# run the client
asyncio.run(start_client())
        