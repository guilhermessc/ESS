import socket

class Server(object):
    def __init__(self, port):
        print('Server is on, port:',port)
        self.__addr = ('192.168.15.9',port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind(self.__addr)
        self.__sock.listen(10)

    def wait_connection(self):
        print('Waiting connection...')
        self.__con, self.__client = self.__sock.accept()
        print('Get connection from:', self.__client)
        return True
    
    def receive(self, b):
        while True:
            data = self.__con.recv(b)
            if len(data) > 0:
                return data
    

