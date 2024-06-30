import socket
def run_tcp_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server's IP address and port
    server_address = ('127.0.0.1', 1234)
    
    # Bind the socket to the server address
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server listening on", server_address)
    
    while True:
        # Wait for a client to connect
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print("Connected from:", client_address)
        
        try:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                
                if not data:
                    break
                
                print("Received from client:", data.decode())
                
                # Send a response back to the client
                message = "Response from server: " + data.decode().upper()
                client_socket.sendall(message.encode())
                
        finally:
            # Close the client socket 
            client_socket.close()

if __name__ == '__main__':
    run_tcp_server()