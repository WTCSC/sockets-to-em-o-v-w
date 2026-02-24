import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (Ask user for ip, if none provided use localhost)
connectip = input("Enter Ip to connect with (none will default to localhost): ")
if connectip:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM):
            socket.settimeout(5) # Set a timeout for connection attempts
            print(f"Attempting to connect to {connectip}:{5000}...")
        
            socket.connect((connectip, 5000))
            print("Connected to server")
        
           # Connection established, proceed with data exchange
            socket.sendall(b'Hello, world')
            data = socket.recv(1024)
            print(f"Received: {data.decode()}")

    except ConnectionRefusedError:
        print(f"Error: Connection to {connectip}:{5000} was  refused. Ensure the server is running on the correct IP.")
    except socket.timeout:
        print(f"Error: Connection timed out. No response from the server within 5 seconds.")
    except socket.gaierror:
        print(f"Address-related error. Check IP address provided: {connectip}.")
    except Exception as e:
        # Catches any other unexpected exceptions
        print(f"An unexpected error occurred: {e}") 
else:
    client.connect(("localhost", 5000))

welcomemsg = client.recv(1024).decode()
print(welcomemsg)
# Send messages and receive responses
question = None
response = None
while True:
    question = client.recv(1024).decode()
    print(f"{question}\n")
    ans = input("Enter Answer: ")
    if not ans:
        break
    client.send(ans.encode())
    response = client.recv(1024).decode()
    print(f"{response}\n")
    response = client.recv(1024).decode()
    print(f"{response}\n")

client.close()