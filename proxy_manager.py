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


#sql _ nnnnnnnnnnnn#######################################
import pymssql,datetime

conn = pymssql.connect(host='100.21.242.146', port=2426, user='avis', password='Jt3$GR+G', database='enterprise')
cursor_mssql = conn.cursor()

ip = str(Received connection from: {}".format(addr))
datee = datetime.datetime.utcnow()
inserteddate = datetime.datetime.strptime(str(datee), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
cursor_mssql.execute("insert into enterprise.dbo.Proxy_management (ip,status,inserteddate) values('%s','%s','%s')" %(ip,1,inserteddate))
conn.commit()


#!111111111111111111

def proxy_manage():



    proxy_client, addr = proxy_manager.accept()
    print("Received connection from: {}".format(addr))


    data = proxy_client.recv(8192)
    dynamic_server.send(data)

    finaldata = dynamic_server.recv(8192)
    proxy_client.send(finaldata)

    #dynamic_server.close()
    proxy_client.close()


while True: 
   proxy_manage()
