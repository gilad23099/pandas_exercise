import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get local machine name
    host = socket.gethostname()
    port = 9999

    # Send a message to the server
    message = "Hello, UDP server!"
    client_socket.sendto(message.encode('utf-8'), (host, port))

    # Receive response from the server
    response, server_address = client_socket.recvfrom(1024)
    print(f"Received response: {response.decode('utf-8')}")

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    start_client()