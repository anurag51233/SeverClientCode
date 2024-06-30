import socket

def run_tcp_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server's IP address and port
    server_address = ('127.0.0.1', 1234)
    
    try:
        # Connect to the server
        client_socket.connect(server_address)
        
        while True:
            # Send data to the server
            message = input("Enter a message to send: ")
            client_socket.sendall(message.encode())
            
            # Receive data from the server
            data = client_socket.recv(1024)
            print("Received from server:", data.decode())
            
            if message.lower() == "exit":
                break
    
    except ConnectionRefusedError:
        print("Connection was refused. Make sure the server is running.")
    
    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    run_tcp_client()