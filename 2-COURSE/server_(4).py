import socket, pickle, threading

SIZE_OF_PART = 10
sock = socket.socket()
sock.bind(('localhost', 8083))

def recieve(connection):
	answer = []
	while True:  # collect the full packet
		part_of_data = connection.recv(SIZE_OF_PART)
		answer.append(part_of_data)
		if len(part_of_data) < SIZE_OF_PART:
			break
	return b''.join(part for part in answer)

def for_thread(conn, addr, counter):
	print('connected:', addr)
	with conn:
		while 1:
			result = recieve(conn)
			conn.send(b'OK')
			print(addr, result)
			if result == b"exit":
				exit()
for i in range(5):
	sock.listen(5)
	conn, addr = sock.accept()
	print("оп")
	threading.Thread(target = for_thread, args = (conn, addr, i,)).start()



print('exit')

sock.close()
