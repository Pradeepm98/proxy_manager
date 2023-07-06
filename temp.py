import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(4096)
    first_line = request.split(b'\n')[0]
    method = first_line.split(b' ')[0]

    if method == b'CONNECT':
        # Extract the requested host and port
        host, port = (first_line.split(b' ')[1].decode('utf-8')).split(':')
        print(host, port)
        # Create a connection to the requested server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((host, int(port)))
        
        # Send the client a success response
        
        # Start forwarding data between client and server
        forward_data(client_socket, server_socket, is_reverse=False)

        server_socket.close()
    else:
        print()

def forward_data(source_socket, destination_socket, is_reverse):
    #source_socket.send(b'HTTP/1.1 200 OK\r\n\r\n')
    source_socket.setblocking(False)
    destination_socket.setblocking(False)
    buffer_size = 4096

    while True:
        try:
            data = source_socket.recv(buffer_size)
            if data:
                    destination_socket.sendall(data)
            else:
                break
        except socket.error:
            pass

        try:
            data = destination_socket.recv(buffer_size)
            if data:
                    source_socket.sendall(data)
            else:
                break
        except socket.error:
            pass
    


def start_proxy_server():
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.connect(('13.127.87.242', 3000))
    print('Connected to proxy server on port 3000')
    while True:
       handle_client(proxy_server)


if __name__ == "__main__":
    start_proxy_server()
