import socket, pickle

SIZE_OF_PART = 1024
sock = socket.socket()
sock.bind(('localhost', 8083))
sock.listen(1)
conn, addr = sock.accept()
def recieve(connection):
	answer = []
	while True:  
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		if len(part_of_data) < SIZE_OF_PART:
			break
	return b''.join(part for part in answer)

print('connected:', addr)
with conn:
	while 1:

		result = recieve(conn)
		index = result.find(b":")
		type_ = result[:index]
		text = result[index+1:]
		if type_ == b"text":
			print(addr, str(text, "UTF-8"))
		if type_ == b"file":
			text = result[index+2:]
			id_ = str(result[index+1: index +2], "UTF-8")
			with open(f"{id_}.jpg", "wb+") as file:
				file.write(text)
					
		conn.send(b'OK')
		if result == b"exit":
			sock.close()




print('exit')

sock.close()
