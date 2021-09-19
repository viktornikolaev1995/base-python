from main import Socket
from threading import Thread

class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        print("Server is listening")
        self.users = []
        self.set_up()
    def set_up(self):
        self.bind(("127.0.0.1", 1234))
        self.listen(5)
        self.start_server()
    def send_data(self, data):
        for user in self.users:
            user.send(data)

    def listen_socket(self, self.listened_socket):
        print("Listening user")
        while True:
            data = self.listened_socket.recv(2048)
            print(f"User sent {data}")
            self.send_data(data)


    def start_server(self):
        while True:
            user_socket, adress = self.accept() #blocking
            print(f"User <{adress[0]}> connected!")
            self.users.append(user_socket)
            listen_accepted_user = Thread(
                target=self.listen_socket,
                args=(user_socket,)
            )
            listen_accepted_user.start()


if __name__ == "__main__":
    Server()