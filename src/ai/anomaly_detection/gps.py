class GPS(object):
	def __init__(self):
		self.__step = 0.05
		self.__first = True
		self.__x_default = -34.8828968
		self.__y_default = -8.0578381
		self.__x_atual = self.__x_default
		self.__y_atual = self.__y_default
	
	def get_location(self):
		if self.__first:
			self.__first = False
			return (self.__x_default, self.__y_default)
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
			
			return (self.__x_atual, self.__y_atual)