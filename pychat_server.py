#
# A python chat progran using TCP sockets with ecryption.
#
# Auther: Oliver S. Neven
# Written in 2016
#
# Server side script
#

import socket, threading, sys, crypt

# Wait for messeges from a connection
def msg_recv(conn, addr):
	nick = ''
	while True:
		try:
			rmsg = fernet.decrypt(conn.recv(2048)).decode('UTF-8')
			if rmsg == '':
				break
			if nick == '':
				nick = rmsg
			else:
				msg_send(addr, nick, rmsg)
		except:
			break
	conns.remove(conn)
	msg_send("", 'SERVER', addr + ' left', False)


# Send a message to all connections
def msg_send(addr, nick, msg, showuser=True):
	if msg != '':
		user = ''
		if showuser:
			user = addr + ' [' + nick + ']: '
		msg = (user + msg).strip()
		print (msg)
		emsg = fernet.encrypt(msg.encode('UTF-8'))
		for conn in conns:
			try:
				conn.send(emsg)
			except:
				conns.remove(conn)

# Accept connections
def accept():
	global conns
	print ('Waiting for clients')
	while True:
		try:
			conn, addr = sock.accept()
			conns.append(conn)

			# Give connection a dedicated thread
			t = threading.Thread(target=msg_recv, args=[conn, addr[0]])
			t.daemon = True
			t.start()

			# Welcome the user
			msg_send('', 'SERVER', addr[0] + ' joined', False)

		except Exception as e:
			print ('Error at socket accept:', str(e))
try:
	host = sys.argv[1]
	port = int(sys.argv[2])
	passwd = sys.argv[3]
except:
	print ('Arguments doesn\'t match')
	sys.exit(404)

fernet = crypt.get_fernet(passwd)
sock = None
conns = []

# Create/bind/listen socket
try:
	sock = socket.socket()
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(999) # Listen for a maximum of 999 clients
except Exception as e:
	print ('Error at socket create/bind/listen:', str(e))
	sys.exit(404)

# Accept clients
a = threading.Thread(target=accept)
a.daemon = True
a.start()

# Chat ! :D
while True:
	smsg = input()
	if smsg == 'exit':
		break
	msg_send("", 'SERVER', smsg)

# Exit
for conn in conns:
	conn.close()
sock.close()
sys.exit(0)
