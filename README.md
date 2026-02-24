# Sockets to Server Quiz Game

A client-server quiz application using Python sockets. The server hosts a quiz game with 25 questions, while the client connects to play and receive scoring feedback.

## Server (`socketsToServer.py`)

- Listens on `0.0.0.0:5000` for incoming connections
- Randomly selects quiz questions from a pool of 25
- Scores responses: +5 points for correct, -5 for incorrect
- Tracks and reports the player's score after each question

## Client (`socketsToClient.py`)

- Prompts user for server IP address (defaults to localhost)
- Connects to the server with a 5-second timeout
- Receives welcome message and quiz questions
- Accepts user input for answers
- Displays feedback and score updates
- Includes error handling for connection failures

## Running the Programs

1. Start the server: `python3 socketsToServer.py`
2. In another terminal, run the client: `python3 socketsToClient.py`
3. Enter the server IP when prompted (or press Enter for localhost)
4. Answer each question with a whole number and press Enter
