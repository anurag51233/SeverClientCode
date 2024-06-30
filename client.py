import socket

def run_tcp_client():
    # Create a socket object with IPv6
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    # Define the server's IPv6 address and port
    server_address = ('[2407:54c0:1b12:ba76:ccc1:5929:3c44:125c]', 7777)
    
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
