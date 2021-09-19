import socket
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
sock.bind(
    ("127.0.0.1", 8888)
)
sock.listen(3)
conn, addr = sock.accept()
print(addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()
