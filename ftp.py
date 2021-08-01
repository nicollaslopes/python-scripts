import socket
from sys import argv
from time import sleep

if(len(argv) != 2):
	print('##################################')
	print('Modo de uso: python3 ftp.py <host>')
	print('##################################')

else:
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	socket.connect((argv[1], 21))

	banner = socket.recv(1024)

	print('Exibindo o banner...')
	sleep(1)
	print(banner)

	print('Entrando com usuário e senha...')
	sleep(1)

	socket.send(b"USER ftp\r\n")
	usuario = socket.recv(1024)

	socket.send(b'PASS ftp\r\n')
	senha = socket.recv(1024)

	print('Enviando comando help')
	sleep(1)
	socket.send(b'help\r\n')
	cmd = socket.recv(2048)
	print(cmd)
