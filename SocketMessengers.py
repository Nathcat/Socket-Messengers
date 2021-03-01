from socket import *
import struct


class Server:
    def __init__(self, port):
        self.s = socket(AF_INET, SOCK_STREAM)

        self.s.bind(("", port))

        self.conn = None
        self.addr = None

    def wait_for_connection(self):
        self.s.listen()

        self.conn, self.addr = self.s.accept()
        print(f"Got connection from {self.addr}.")

    def receive_message(self):
        if self.conn == None or self.addr == None:
            print("Socket is not connected!")
            return

        raw_msglen = self.conn.recv(4)
        msglen = struct.unpack('>I', raw_msglen)[0]

        total = 0
        total_data = b""
        while len(total_data) < msglen:
            data = self.conn.recv(msglen)
            total_data += data
            total += len(data)

        return total_data


class Client:
    def __init__(self):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.addr = None

    def connect(self, host, port):
        try:
            self.addr = (host, port)
            self.s.connect(self.addr)
        except ConnectionRefusedError:
            print(f"Connection was refused at address ({host}, {port}).")

    def send(self, data):
        data = struct.pack(">I", len(data)) + data

        try:
            self.s.sendall(data)
        except Exception as e:
            print(f"An error occurred: {e}")

    def kill(self):
        self.s.shutdown(SHUT_RDWR)
