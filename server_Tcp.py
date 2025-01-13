import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 9999

    # Bind to the port
    server_socket.bind((host, port))

    # Start listening for clients
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    # Establish a connection
    client_socket, addr = server_socket.accept()

    print(f"Got a connection from {addr}")

    # Receive message from the client
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received message: {message}")

    # Send a response back to the client
    response = "Message received"
    client_socket.send(response.encode('utf-8'))

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_server()
