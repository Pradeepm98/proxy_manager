import socket

dynamic = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dynamic.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "0.0.0.0"
port = 30000

dynamic.bind((host, port))
print("Server is listening on {}:{}".format(host, port))

dynamic.listen(5)
print("Server is listening on {}:{}".format(host, port))

proxy_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_manager.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "0.0.0.0"
port = 30001

proxy_manager.bind((host, port))
print("Server is listening on {}:{}".format(host, port))

proxy_manager.listen(5)
print("Server is listening on {}:{}".format(host, port))

try:
    dynamic_server, addr = dynamic.accept()
    print("Received connection from: {}".format(addr))

    proxy_client, addr = proxy_manager.accept()
    print("Received connection from: {}".format(addr))

    data = proxy_client.recv(10240)
    dynamic_server.send(data)

    finaldata = dynamic_server.recv(10240)
    proxy_client.send(finaldata)

finally:
    dynamic_server.close()
    proxy_client.close()
    dynamic.close()
    proxy_manager.close()
