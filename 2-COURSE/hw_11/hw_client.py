import socket
from threading import Thread
import time
import argparse
import random
import pickle


SIZE_OF_PART = 1024

class Client:
	def __init__(self, ip, port, num):
		self.num = num
		self.time = input("Введите интервал : ")
		self.connect(ip, port)

	def recieve(self):
		return self.sock.recv(SIZE_OF_PART).decode('UTF-8')

	def send(self):
		time.sleep(float(self.time))
		data = "client -".encode('UTF-8')
		self.sock.send(data)

	def read_socket(self):
		while 1:
			data = self.recieve()
			print(data)

	def loop(self):

		self.thread = Thread(target=self.read_socket)
		self.thread.start()
		while True:
			time.sleep(float(self.time))

			with open(f"client_{self.num}.pickle", "rb+") as f:
				list_ = [random.randint(1, 10) for _ in range(10)]
				pickle.dump(list_, f)
				self.sock.send('OK'.encode("UTF-8"))

	def connect(self, ip, port):
		self.sock = socket.socket()
		self.sock.connect((ip, port))
		with open(f"client_{self.num}.pickle", "ab") as f:
			pass
		self.sock.send(f'{self.num}'.encode())
		self.loop()

	def disconnect(self):
		self.thread.join()
		self.sock.close()
		print('exit')


parser = argparse.ArgumentParser("бла бла")
parser.add_argument('integers', type=int, nargs=1)
args = parser.parse_args()
num = args.integers

client = Client('localhost', 8081, num[0])
client.loop()
