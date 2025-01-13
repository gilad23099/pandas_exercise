import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 9999

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    # Send a message to the server
    message = "Hello, server!"
    client_socket.send(message.encode('utf-8'))

    # Receive response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received response: {response}")

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()
