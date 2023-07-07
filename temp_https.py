import socket

dynamic = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dynamic.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "0.0.0.0"
port = 3000

dynamic.bind((host, port))
print("Server is listening on {}:{}".format(host, port))

dynamic.listen(1)
print("Server is listening on {}:{}".format(host, port))

proxy_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_manager.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "0.0.0.0"
port = 3001

proxy_manager.bind((host, port))
print("Server is listening on {}:{}".format(host, port))

proxy_manager.listen(1)
print("Server is listening on {}:{}".format(host, port))




#!1#######################################################

def proxy_manage():


    dynamic_server, addr = dynamic.accept()
    print("Received connection from: {}".format(addr))
    print(type(addr))



    proxy_client, addr = proxy_manager.accept()
    print("Received connection from: {}".format(addr))


    data = proxy_client.recv(4096)
    print(data)
    dynamic_server.sendall(data)
    proxy_client.send(b'HTTP/1.1 200 OK\r\n\r\n')



    dynamic_server.setblocking(False)
    proxy_client.setblocking(False)
    buffer_size = 4096

    while True:
        
        try:
            print('hiii')
            data = proxy_client.recv(buffer_size)
            print("da2a")
            if data:
                    dynamic_server.sendall(data)
            else:
                break
        except socket.error:
            pass

        try:
            data = dynamic_server.recv(buffer_size)
            if data:
                    proxy_client.sendall(data)
            else:
                break
        except socket.error:
            pass

    

    dynamic_server.close()
    proxy_client.close()


while True: 
   proxy_manage()
