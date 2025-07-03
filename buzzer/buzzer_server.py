import asyncio
import websockets

# Global variable: A list to store all clients who have buzzed in
# Each item will be a tuple: (websocket_connection, time_they_buzzed)
# creat an empty list to store connected clients

clients = []

# Function to handle incoming messages from clients
async def handle_message(websocket):
    """
    This function runs every time a client sends a message to the server

    Args:
        websocket: The connection to the client who sent the message
        path: The URL path the client connected to (not used in this example)
    """
    # Tell Python we want to use the global variables (not create new local ones)
    global clients
    global fastest_time
    try:
        # Keep listening for messages from this client
        message= await websocket.recv()
        if message == "buzz":
                response_time = asyncio.get_event_loop().time()
                clients.append((websocket, response_time))
                if len(clients) == 1:
                    await websocket.send("first place!")  
                    fastest_time = response_time
                else:
                    t = round(response_time - fastest_time, 2)
                    await websocket.send(f"response time :{t} seconds slower !")    
    except websockets.exceptions.ConnectionClosed:
        pass
            
# run the server
async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

asyncio.run(start_server())
        