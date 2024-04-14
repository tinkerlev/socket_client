#eliran 13:48
import socket

def create_client():
    # Prompt the user to enter the IP address of the server.
    ip = input("Enter the server IP address: ")

    # Prompt the user to enter the port number and convert it to an integer.
    port = int(input("Enter the port number: "))

    # Create a new socket using IPv4 and TCP/IP protocols.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server using the provided IP and port.
        s.connect((ip, port))

        # Define a message to send to the server.
        message = "Hello, server!"

        # Send the message. The `encode()` method converts the string into bytes.
        s.sendall(message.encode())

        # Wait to receive data from the server, up to 1024 bytes.
        data = s.recv(1024)

        # Decode the received bytes back into a string and print it.
        print("Received from server:", data.decode())

# Call the function to execute the client code.
create_client()
