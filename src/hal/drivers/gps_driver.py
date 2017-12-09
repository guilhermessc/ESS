
import sys
from socket import *

x = -34.8828968
y = -8.0578381

SERVER_IP = 'localhost'
### Caso queira alterar essa porta lembre-se de altere tambem no client ###
PORT_NUMBER_SERVER = 10003


sock = socket(AF_INET, SOCK_STREAM)
sock.connect( (SERVER_IP, PORT_NUMBER_SERVER) )

message = ""
while True:
	# Enviando
	step = 0.05

	walk = input("Input your direction:")

	if walk == "w":
		y = y + step
	if walk == "s":
		y = y - step 
	if walk == "a": 
		x = x + step
	if walk == "d":
		x = x - step

	message = str(x) + ',' + str(y)
# aqui ficariam os dados do GPS
	sock.sendall(message.encode('utf-8'))

sock.close()