import math

class SP(object):
    def __init__(self, file_name):
        self.__secure = []
        self.__file = open(file_name)
        
        ordem = 0
        x = ''
        y = ''
        orig = ''
        dest = ''
        p_x = 0.0
        p_y = 0.0
        
        #Lê o arquivo e armazena na forma lista de lista de tuplas
        #Formato de cada linha: [(origem:destino);(p1_x,p1_y);(p2_x, p2_y);...;(pn_x,pn_y)]
        for line in self.__file:
            lista = []
            trigger = True
            for c in line:
                if trigger:
                    if c == ';':
                        trigger = False
                    elif c == '(' or c == '[':
                        continue
                    elif c == ':':
                        ordem += 1
                    elif c == ')':
                        lista.append((orig,dest))
                        ordem = 0
                        orig = ''
                        dest = ''
                    else:
                        if ordem%2 == 0:
                            orig += c
                        else:
                            dest += c

                else:
                    if c == '(' or c == '[' or c == ']' or c == ';':
                        continue
                    elif c == ',':
                        p_x = float(x)
                        ordem += 1
                        x = ''
                    elif c == ')':
                        p_y = float(y)
                        y = ''
                        ordem = 0
                        lista.append((p_x, p_y))
                    else:
                        if ordem%2 == 0:
                            x += c
                        else:
                            y += c
            self.__secure.append(lista)

    def show_paths(self):
        print("\nPaths: ", len(self.__secure))
        for path in self.__secure:
            print('\t',path)
    
    def verify(self, orig_place, x, y):
        for path in self.__secure:
            if path[0][0] == orig_place:
                #make sliding window
                for i in range(2,len(path)):
                    l_a = i-1
                    l_b = i
                    l_c = i+1
                    if self.dist()
        return (False, '')