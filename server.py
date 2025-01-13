import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get local machine name
    host = socket.gethostname()
    port = 9999

    # Bind to the port
    server_socket.bind((host, port))

    print(f"UDP Server listening on {host}:{port}")

    # Receive message
    message, addr = server_socket.recvfrom(1024)
    print(f"Received message: {message.decode('utf-8')} from {addr}")

    # Send a response back to the client
    response = "Message received"
    server_socket.sendto(response.encode('utf-8'), addr)

    # Close the socket
    server_socket.close()

if __name__ == '__main__':
    start_server()
