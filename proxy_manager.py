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

dynamic_server, addr = dynamic.accept()
print("Received connection from: {}".format(addr))

def proxy_manage():



    proxy_client, addr = proxy_manager.accept()
    print("Received connection from: {}".format(addr))


    data = proxy_client.recv(1024)
    dynamic_server.send(data)

    finaldata = dynamic_server.recv(1024)
    proxy_client.send(finaldata)

    #dynamic_server.close()
    proxy_client.close()


while True: 
   proxy_manage()
