from socket import *

class Client(object):
	__raspSock = []
	__raspIP = '192.168.25.12'
	__raspPort = 4513 

	def __init__(self):
		self.initRasp()
		self.raspLoop()
		self.close()

	def initRasp(self):
		self.__raspSock = socket(AF_INET, SOCK_STREAM)
		#self.__raspIP = gethostbyname(gethostname())

	def raspLoop(self):
		self.__raspSock.connect((self.__raspIP, self.__raspPort))
		while True:
			message = input("Digite uma mensagem:")
			self.__raspSock.send(message.encode('utf-8'))

	def close(self):
		self.__raspSock.close()

c1 =  Client()
c1.close()