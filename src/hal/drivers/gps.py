#!/usr/bin/env python3

import socket

class GPS(object):
	def __init__(self, address):
		self.__step = 0.05
		self.__first = True
		self.__x_default = -8.038505
		self.__y_default = -34.914499
		self.__x_atual = self.__x_default
		self.__y_atual = self.__y_default

		#socket
		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__addr = address
		self.__sock.connect(self.__addr)

	def get_location(self):
		if self.__first:
			self.__first = False
			string = str(self.__x_default) + ',' + str(self.__y_default)
			self.__sock.send(string.encode())
		else:
			walk = input('Simulate step direction [P/N/S/L/O]: ')
			if walk == 'N':
				self.__y_atual += self.__step
			elif walk == 'S':
				self.__y_atual -= self.__step
			elif walk == 'L':
				self.__x_atual += self.__step
			elif walk == 'O':
				self.__x_atual -= self.__step
			elif walk == 'P':
				pass
			else:
				print("Direction not valid, try again.")

			string = str(self.__x_atual) + ',' + str(self.__y_atual)
			self.__sock.send(string.encode())



#--------   MAIN --------
gps = GPS(('192.168.15.9',7000))
while True:
    gps.get_location()
