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
	return b''.join(part for part in answer)

with sock:
	while 1:
		type_  = input("тип : ").encode("utf-8")
		if type_ == b"text":
			text = input("текст : ").encode("utf-8")
			msg = b"" + type_ + b":" + text
			sock.send(msg)
			continue
		if type_ := b"file":
			id_ = input("id file : ").encode("utf-8")
			file_path = input("путь файла : ")
			with open(file_path, "rb") as file:
				data = b''.join(file)
				msg = b"" + type_ + b":" + id_ + data
				sock.send(msg)
		answer = recieve(sock)
		print("get from server: ", answer)

