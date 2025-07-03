# WebSockets Example

A simple WebSocket client-server example using Python's `websockets` library.

## Description

This project demonstrates basic WebSocket communication between a client and server:
- The server listens on `ws://localhost:8765`
- The client connects to the server and sends a name
- The server receives the name and sends back a greeting
- Both client and server print the messages they send/receive

## Files

- `server.py` - WebSocket server that receives names and sends greetings
- `client.py` - WebSocket client that sends a name and receives a greeting
- `requirements.txt` - Python dependencies

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python server.py
```

2. In another terminal, run the client:
```bash
python client.py
```

3. Enter your name when prompted and see the greeting exchange!

## Requirements

- Python 3.7+
- websockets library

## Example Output

**Server output:**
```
Server started on ws://localhost:8765
Hello Alice!
Sent: Hello Alice!
```

**Client output:**
```
Enter your name: Alice
Sent: Alice
Received: Hello Alice!
```
