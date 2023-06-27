# %%
import socket

# Create a socket object
dynamic = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and define a port for communication
host = "0.0.0.0"#socket.gethostname()
port = 30000

# Bind the socket to a specific address and port
dynamic.bind((host, port))
print("Server is listening on {}:{}".format(host, port))

# Listen for incoming connections
dynamic.listen(5)

print("Server is listening on {}:{}".format(host, port))

# %%
import socket

# Create a socket object
proxy_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and define a port for communication
host = "0.0.0.0"#socket.gethostname()
port = 30001

# Bind the socket to a specific address and port
proxy_manager.bind((host, port))
print("Server is listening on {}:{}".format(host, port))

# Listen for incoming connections
proxy_manager.listen(5)

print("Server is listening on {}:{}".format(host, port))

# %%
dynamic_server, addr = dynamic.accept() 
print("Received connection from: {}".format(addr))

# %%
proxy_client, addr = proxy_manager.accept() 
print("Received connection from: {}".format(addr))

# %%
limit = 1
while limit < 5:
    data = proxy_client.recv(1024)

    dynamic_server.send(data)

    finaldata=dynamic_server.recv(1024)

    proxy_client.send(finaldata)

    limit +=1
