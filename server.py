import socket
import threading

class CommandServer:
 
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None

    def handle_client(self, connection, address):
        print(f"[NEW CONNECTION] {address} connected")

        connected = True
        while connected:
            msg_length = connection.recv(1024)

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.host}")
        
        try:
            while True:
                connection, address = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(connection, address))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        except KeyboardInterrupt:
            print("Shutting server down")
        finally: 
            self.server.close()

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 9672

    command_server = CommandServer(HOST, PORT)
    command_server.start()

