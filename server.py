import asyncio 
import websockets

async def hello(websocket):
    """
    Receives a name from the websocket, prints a greeting, and sends the greeting back.

    Args:
        websocket: The websocket connection to communicate with the client.
    """
    # Receive a name from the client over the websocket
    name = await websocket.recv()
    print(f"Hello {name}!")

    # Prepare a greeting message
    greeting = f"Hello {name}!"
    # Send the greeting back to the client
    await websocket.send(greeting)
    print(f"Sent: {greeting}")

async def main():
    """
    Main function to start the websocket server.
    """
    # Start the websocket server on port 8765
    async with websockets.serve(hello, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever
if __name__ == "__main__":
    # Run the main function to start the server
    asyncio.run(main())