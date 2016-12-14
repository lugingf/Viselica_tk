# coding: utf-8

import socket
import sys

HOST = 'localhost'
PORT = 7777

print('Клиент игры "Виселица"')
print('Подкоючение к серверу...')

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
except:
	print('Ошибка подключения к серверу')
	sys.exit(13)

try:
	sock.sendall(bytes('START', 'utf-8'))
	received = str(sock.recv(1024), 'utf-8')
except:
	sock.close()
	print('Ошибка отправки START')
	sys.exit(14)

data = received.split(';')
if data[0] == 'GUESS':
		print('Угадай число: {} < x < {}'.format(data[1], data[2]))
		
		while True:
			x = input("Ваш ответ (q - для выхода): ")
			if x == 'q':
				sock.sendall(bytes("GOODBYE", "utf-8"))
				break
			try:
				sock.sendall(bytes('TRY;{}'.format(x), "utf-8"))
				received = str(sock.recv(1024), "utf-8")
			except:
				print("Ошибка отправки серверу")
				break
				
			data = received.split(';')
			if data[0] == 'TRUE':
				print('Вы угадали!')
				break
			elif data[0] == 'FALSE':
				if data[2] == '<':
					print('Вы не угадали. Число меньше. Осталось попыток: {}'.format(data[1]))
				else:
					print('Вы не угадали. Число больше. Осталось попыток: {}'.format(data[1]))
			elif data[0] == 'FAIL':
				print('Вы не угадали и проиграли!')
				break
		sock.close()
else:
	print('Неизвестный ответ сервера')
	
		
	#  START - GUESS;1;100
	#  TRY;x - TRUE
	#        - FALSE;y;<
	#        - FALSE;y;>
	#		 - FAIL
	#  GOODBYE - GOODBYE