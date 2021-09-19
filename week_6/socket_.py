import socket
connection = socket.create_connection(('127.0.0.1', 8888))
# command = 'got *\n'
# command = 'get 1 2\n'
# command = 'put palm.cpu 23.7 1150864247 34\n'

connection.sendall(command.encode())
data = connection.recv(2048).decode("utf-8")
connection.close()
print(ascii(data))