from socket import *

class Server(object):
	__clientList = list
	__serverPort = 4513
	__serverIP = '192.168.25.12'
	__serverSock = []

	def __init__(self):
		self.initCloud()
		print("Hello, server is on!\nIP:",self.__serverIP," Port:",self.__serverPort)
		self.cloudLoop()
		self.close()

	def initCloud(self):
		self.__serverSock = socket(AF_INET, SOCK_STREAM)
		self.__serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		#self.__serverIP = gethostbyname(gethostname())
		self.__serverSock.bind( (self.__serverIP, self.__serverPort) )
		self.__serverSock.listen(1)

	def cloudLoop(self):
		while True:
			cloudConnection, clientAddr = self.__serverSock.accept()
			print("Recieved connection from:",clientAddr)
			while True:
				data = cloudConnection.recv(1024) 
				data = data.decode('utf-8')
				print(data)

	def close(self):
		self.__serverSock.close()

s = Server()
s.close()