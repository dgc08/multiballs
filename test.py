import socket

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Replace with the server's IP address or hostname
    PORT = 47434  # Replace with the server's port number

    # Create a socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Prepare the data to be sent
        instruction = "Your instruction here"

        # Encode the data and send it to the server
        s.sendall(instruction.encode('utf-8'))