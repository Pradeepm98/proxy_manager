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
print(type(addr))

#sql _ nnnnnnnnnnnn#######################################
# import pymssql,datetime

# conn = pymssql.connect(host='100.21.242.146', port=2426, user='avis', password='Jt3$GR+G', database='enterprise')
# cursor_mssql = conn.cursor()

# ip = addr[0]
# print(type(ip))
# print(type(ip))
# proxy='13.127.87.242:3001'
# datee = datetime.datetime.utcnow()
# inserteddate = datetime.datetime.strptime(str(datee), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
# cursor_mssql.execute("insert into enterprise.dbo.Proxy_management (ip,status,inserteddate,proxy) values('%s','%s','%s','%s')" %(ip,1,inserteddate,proxy))
# conn.commit()


#!111111111111111111

def proxy_manage():



    proxy_client, addr = proxy_manager.accept()
    print("Received connection from: {}".format(addr))


    data = proxy_client.recv(4096)
    dynamic_server.sendall(data)
    print(data)
    proxy_client.send(b'HTTP/1.1 200 OK\r\n\r\n')
 

    dynamic_server.setblocking(False)
    proxy_client.setblocking(False)
    buffer_size = 4096

    while True:
        try:
            data = proxy_client.recv(buffer_size)
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



    #dynamic_server.close()
    proxy_client.close()


while True: 
   proxy_manage()
   print('hello')
