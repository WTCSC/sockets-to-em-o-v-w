import socket
import random

# Quiz Questions
questions = [
    "How many planets are in our solar system?",
    "How many continents are there on Earth?",
    "How many sides does a hexagon have?",
    "How many players are on the field for one team in soccer?",
    "In what year did World War II end?",
    "How many stripes are on the flag of the United States?",
    "How many bones are in the adult human body?",
    "How many keys are there on a standard piano?",
    "How many time zones are there in Russia?",
    "In what year did Jurassic Park premiere?",
    "How many amendments does the United States Constitution have?",
    "How many hearts does an octopus have?",
    "How many players are there on a standard basketball team on the court at one time?",
    "How many days are there in a leap year?",
    "In what year did Tokyo host its first Summer Olympics?",
    "How many squares are there on a standard chessboard?",
    "How many strings does a standard violin have?",
    "How many U.S. states border Canada?",
    "In what year did NASA land the first humans on the Moon?",
    "How many tentacles does a squid typically have?",
    "How many elements are on the periodic table as of 2026?",
    "How many cards are in a standard deck (without jokers)?",
    "In what year did The Lion King release?",
    "How many degrees are in a right angle?",
    "How many boroughs make up New York City?"
]

answers = [
    8,
    7,
    6,
    11,
    1945,
    13,
    206,
    88,
    11,
    1993,
    27,
    3,
    5,
    366,
    1964,
    64,
    4,
    13,
    1969,
    10,
    118,
    52,
    1994,
    90,
    5
]

# Create a socket object, IPv4 and TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to 0.0.0.0:5000
server.bind(("0.0.0.0", 5000))

# Wait for connections
server.listen(1)
print("Waiting for a connection.")

# Client connection
client, addr = server.accept()
print(f"Connected to {addr}")

# Needed variables for Quiz game
qNum = None
Ans = None
Score = 0

# Receive and echo questions and answers
client.send(("Welcome to the SocketsToServer Quiz Game, the server will send you questions and then raise or lower your score based on your answer, all questions will have whole number answers Ex: 1,10,50 etc").encode())
while True:
    qNum = random.randint(0,len(questions)-1)
    client.send((f"Current Question: {questions[qNum]}").encode())
    Ans = client.recv(1024).decode()
    if not Ans:
        break
    print(f"Received: {Ans}")
    if int(Ans) == answers[qNum]:
        client.send(f"Correct answer received: {Ans}, +5 points".encode())
        Score += 5
    else:
        client.send(f"Incorrect answer received: {Ans}, -5 points".encode())
        Score -= 5

    client.send((f"Current Score: {Score}").encode())

client.close()
server.close()