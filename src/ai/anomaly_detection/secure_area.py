import math

class SA(object):
    def __init__(self, file_name):
        self.__secure = []
        self.__file = open(file_name)

        #lê arquivo e armazena todas as zonas seguras em uma lista
        for line in self.__file:
            trigger = True
            ordem = 1
            x = ''
            y = ''
            z = ''
            w = ''
            tag = ''
            x_float = 0.0
            y_float = 0.0
            z_float = 0.0
            w_float = 0.0

            for c in line:
                if c == '(':
                    trigger = False
                    continue
                if trigger:
                    tag += c
                else: 
                    if(c == '('):
                        continue
                    elif(c == ',' or c == ')'):
                        if ordem == 1:
                            x_float = float(x)
                        elif ordem == 2:
                            y_float = float(y)
                        elif ordem == 3:
                            z_float = float(z)
                        else:
                            w_float = float(w)
                        ordem += 1
                    else:
                        if(ordem == 1):
                            x += c
                        elif ordem == 2:
                            y += c
                        elif ordem == 3:
                            z += c
                        else:
                            w += c
                    raio = self.dist2points(x_float, y_float, z_float, w_float)
                
            #adiciona lugar seguro na lista
            lista = [tag,x_float, y_float, raio]
            self.__secure.append(lista)
        
        if len(self.__secure) < 2:
            print("Devem ser cadastradas pelo menos 2 areas seguras")


    def dist2points(self, x1, y1, x2, y2):
        dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        return dist
    
    def show_areas(self):
        print("Numero de Safe Areas:", len(self.__secure))
        for sublist in self.__secure:
            print("\t",sublist)
        
    def verify(x, y):
        for area in self.__secure:
            dist = math.sqrt(math.pow(x - area[1], 2) + math.pow(y - area[2], 2))
            if dist < area[3]:
                return (True, area[0])
        return (False, '')
