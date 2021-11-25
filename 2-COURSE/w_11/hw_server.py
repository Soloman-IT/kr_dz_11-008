import socket
import threading
import time
from threading import Thread
import pickle

BUFFER = 1024


class Client:
    def __init__(self):
        self.__address = None
        self.__connection = None
        self.__name = None
        self.__num = None

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, x):
        self.__num = x


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        self.__name = x

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, x):
        self.__address = x

    @property
    def connection(self):
        """
        Returns:
            socket.socket: connection
        """
        return self.__connection

    @connection.setter
    def connection(self, x):
        self.__connection = x

class Server:
    def __init__(self, ip, port):
        self.delete = False
        self.clients = set()
        self.sock = socket.socket()
        self.sock.bind((ip, port))
        self.listen()

    def listen(self):
        print('Start')
        self.sock.listen()
        while True:
            connection, address = self.sock.accept()
            if self.delete:
                exit()
            num = connection.recv(BUFFER)
            client = Client()
            client.address = address
            client.connection = connection
            client.num = int(num.decode())

            self.clients.add(client)

            print(f'Connected {address}')
            Thread(target=self.recv_file, args=(client, )).start()

    def recv_file(self, client, new_client=False):
        try:
            while 1:
                flag = client.connection.recv(BUFFER)
                print(flag.decode())
                with open(f"client_{client.num}.pickle", "rb") as f:
                    data = pickle.load(f)
                    print(data, "from", f" client_{client.num}")
                    self.send_all(client, f'client_{client.num} ', data)
                    print("передал")
        except Exception:
            self.close_client(client)
            return False
        else:
            return True
    # def recv_and_share(self, client, new_client=False):
    #     try:
    #         self.lock.acquire()
    #         if response := client.connection.recv(BUFFER):
    #             response = response.decode('UTF-8')
    #             if new_client:
    #                 client.name = response
    #                 print(f'new client {client.address} with name: {response}')
    #                 self.send_all(client, 'Привет всем, я новенький!')
    #             else:
    #                 print(f'from client {client.address} recieved: {response}')
    #                 self.send_all(client, response)
    #         else:
    #             raise Exception('Client disconnected')
    #     except Exception:
    #         self.close_client(client)
    #         return False
    #     else:
    #         return True

    def client_loop(self, client):
        """

        Args:
            client (Client):

        Returns:

        """

        self.recv_file(client, new_client=True)
        while self.recv_file(client):
            pass

    def send_all(self, from_client, text_client, text):
        print(self.clients)
        for client in self.clients:
            if client != from_client:
                client.connection.send(f"[{text_client}]: {text}".encode('UTF-8'))

    def close_client(self, client):
        self.clients.remove(client)
        print('remove : ', client)
        client.connection.close()
        print(self.clients)
        if (self.clients) == set():
            self.delete = True


server = Server('localhost', 8081)