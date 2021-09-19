import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 10001))
sock.listen(socket.SOMAXCONN)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf8"))

conn.close()
sock.close()