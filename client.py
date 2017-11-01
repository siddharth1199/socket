## Client for Multiple Client ChatServer

import socket 

def join():
	chatroom = input('Enter Chatroom name to enter')

	conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
	conn_msg += "CLIENT IP: \n".encode('utf-8')
	conn_msg += "PORT: \n".encode('utf-8')
	conn_msg += "CLIENT_NAME:".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')

	s.send(conn_msg)

def chat():
	pass

def leave():
	
	conn_msg += "JOIN_ID".encode('utf-8') + str(clThread.uid).encode('utf-8')
	conn_msg += "LEAVE_CHATROOM:".encode('utf-8')

	s.send(conn_msg)

def discon():
	pass

# create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
 
# get local machine name 
host = input('Enter Hostname')
 
port = 50000 
# connection to hostname on the port. 
s.connect((host, port))                                

Cname = input('Give Client Name')
join()

while(1):
	message = s.recv(1024)
	print('Enter Option to choose:')
	print('1. Join')
	print('2. Chat')
	print('3. Leave')
	print('4. Disconnect')
	task = input('')
	if task == 1:
		join()
	elif task == 2:
		chat()
	elif task == 3:
		leave()
	elif task == 4:
		discon()
	elif task == 5:
		print('Error')
	

