import socket, pickle

# prepare
SIZE_OF_PART = 10
sock = socket.socket()
sock.connect(('localhost', 8083))


def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		if len(part_of_data) < SIZE_OF_PART:
			break
	return ''.join(part.decode('UTF-8') for part in answer)

with sock:
	while 1:
		text = input().encode()
		sock.send(text)
		answer = recieve(sock)
		print("get from server: ", answer)
		if text == "exit":
			break

