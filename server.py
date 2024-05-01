import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 8888)

# Bind the socket to the address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Bank server is up and running...")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        print("Received:", data)

        # Parse the client's request
        request = data.decode().strip().split()
        if len(request) != 5 or request[0] != "transfer":
            client_socket.sendall(b"Invalid request format")
            continue

        # Extract the transfer details
        amount = float(request[2])
        from_account = request[1]
        to_account = request[4]

        # Process the transfer (e.g., update account balances)
        print(f"Processing transfer of ${amount} from {from_account} to {to_account}")

        # Send a response back to the client
        client_socket.sendall(b"Transaction successful")

    finally:
        # Clean up the connection
        client_socket.close()
