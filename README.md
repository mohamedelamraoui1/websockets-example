# WebSockets Example

A collection of WebSocket client-server examples using Python's `websockets` library.

## Description

This project demonstrates basic WebSocket communication between clients and servers with two different examples:

### Basic Example
- The server listens on `ws://localhost:8765`
- The client connects to the server and sends a name
- The server receives the name and sends back a greeting
- Both client and server print the messages they send/receive

### Buzzer System Example
- A game show-style buzzer system where multiple clients can compete
- First client to press spacebar gets "first place!"
- Subsequent clients get their response time compared to the winner
- Demonstrates real-time competitive interaction between multiple clients

## Files

### Basic Example
- `server.py` - WebSocket server that receives names and sends greetings
- `client.py` - WebSocket client that sends a name and receives a greeting

### Buzzer System
- `buzzer/buzzer_server.py` - WebSocket server that handles buzzer competition
- `buzzer/buzzer_client.py` - WebSocket client that sends buzz signals on spacebar press

### Other Files
- `requirements.txt` - Python dependencies

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

1. Start the server:
```bash
python server.py
```

2. In another terminal, run the client:
```bash
python client.py
```

3. Enter your name when prompted and see the greeting exchange!

### Buzzer System Example

1. Start the buzzer server:
```bash
python buzzer/buzzer_server.py
```

2. In separate terminals, run multiple buzzer clients:
```bash
python buzzer/buzzer_client.py
```

3. Press the spacebar in any client window to buzz in! The first to press gets first place, others get their delay time.

## Requirements

- Python 3.7+
- websockets library
- keyboard library (for buzzer system)

## Example Output

### Basic Example

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

### Buzzer System Example

**Server output:**
```
Server started on ws://localhost:8765
```

**First client output:**
```
Received: first place!
```

**Second client output:**
```
Received: response time: 1.23 seconds slower!
```
