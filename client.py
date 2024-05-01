import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 8888)

# Connect to the server
client_socket.connect(server_address)

# Prompt the user for the transfer details
from_account = input("Enter the account to transfer from: ")
to_account = input("Enter the account to transfer to: ")
amount = float(input("Enter the amount to transfer: "))

# Construct the request message
request = f"transfer {from_account} {amount} to {to_account}"

# Send the request to the server
client_socket.sendall(request.encode())

# Receive the response from the server
response = client_socket.recv(1024)
print("Response from server:", response.decode())

# Close the connection
client_socket.close()
