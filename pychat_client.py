#
# A python chat progran using TCP sockets with ecryption.
# 
# Auther: Oliver S. Neven
# Written in 2016
#
# Client side script
#

import socket, threading, sys, crypt

# Wait for messages from the server
def msg_recv(sock):
	while True:
		try:
			rmsg = fernet.decrypt(sock.recv(2048)).decode('UTF-8')
			if rmsg == '':
				break
			print (rmsg)
		except:
			break
	print ('Server closed')
	sock.close()
	sys.exit(404)


try:
	host = sys.argv[1]
	port = int(sys.argv[2])
	passwd = sys.argv[3]
	nick = sys.argv[4]
except:
	print ('Arguments doesn\'t match')
	sys.exit(404)

fernet = crypt.get_fernet(passwd)
sock = None

# Create socket
try:
	sock = socket.socket()
except Exception as e:
	print ('Failed to create socket:', str(e))
	exit (404)

# Connect to server
try:
	sock.connect((host, port))
	sock.send(fernet.encrypt(nick.encode('UTF-8')))
except Exception as e:
	print ('Failed to connect to server:', str(e))
	exit (404)

# Chat ! :D
recv = threading.Thread(target=msg_recv, args=[sock])
recv.daemon = True
recv.start()
while True:
	smsg = input()
	if smsg == 'exit':
		break
	if smsg == '':
		continue
	try:
		sock.send(fernet.encrypt(smsg.encode('UTF-8')))
	except Exception as e:
		print ('Failed to send message:', str(e))

sock.close()
sys.exit(0)
