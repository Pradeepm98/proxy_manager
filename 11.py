import socket
import threading

def temp(dynamic_port, proxy_port):

    dynamic = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dynamic.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = "0.0.0.0"
    # dynamic_port = 3000

    dynamic.bind((host, dynamic_port))

    dynamic.listen(1)
    print("Server is listening on {}:{}".format(host, dynamic_port))

    proxy_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_manager.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = "0.0.0.0"
    # proxy_port = 3001

    proxy_manager.bind((host, proxy_port))

    proxy_manager.listen(1)
    print("Server is listening on {}:{}".format(host, proxy_port))

    # dynamic_server, addr = dynamic.accept()
    # print("Received connection from: {}".format(addr))
    # print(type(addr))




    def proxy_manage():

        dynamic_server, addr = dynamic.accept()
        print("Received connection from proxy :  {}".format(addr))
        print(type(addr))

        proxy_client, addr = proxy_manager.accept()
        print("Received connection from client : {}".format(addr))

        data = proxy_client.recv(8192)
        print(data)
        dynamic_server.sendall(data)
        proxy_client.send(b'HTTP/1.1 200 OK\r\n\r\n')

        # dynamic_server.setblocking(False)
        # proxy_client.setblocking(False)
        buffer_size = 8192
        def t():

          while True:

            try:
                # print('hiii')
                data = proxy_client.recv(buffer_size)
                # print("da2a")
                if data:
                    dynamic_server.sendall(data)
                else:
                    break
            except socket.error:
                pass

        def t2():
          while True:
            try:
                data = dynamic_server.recv(buffer_size)
                if data:
                    proxy_client.sendall(data)
                else:
                    break
            except socket.error:
                pass

        thread1 = threading.Thread(target=t).start()
        thread2 = threading.Thread(target=t2).start()


        # dynamic_server.close()
        # proxy_client.close()


    while True:
      proxy_manage()



if __name__ == '__main__':
    threading.Thread(target=temp, args=(30000, 30001)).start()
    threading.Thread(target=temp, args=(30002, 30003)).start()
    threading.Thread(target=temp, args=(30004, 30005)).start()
