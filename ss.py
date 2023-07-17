import socket

def handle_client(client_socket):
    print("New client connected")
    #client_socket.send(b"Hi")
    
    while True:
        try:
            data = client_socket.recv(1024)
            print(data)
            if not data:
                print("Client disconnected")
                break
        except ConnectionResetError:
            print("Client forcibly closed the connection")
            break

    client_socket.close()

def start_server():
    host = '0.0.0.0'  # localhost
    port = 30000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, port))

    while True:
        client_socket, address = server_socket.accept()
        handle_client(client_socket)

start_server()
