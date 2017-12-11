import math

class SP(object):
    def __init__(self, file_name):
        self.__secure = []
        self.__possibilidades = []
        self.__file = open(file_name, 'r')
        self.__filename = file_name
        self.__caminho = False
        self.__pathway = []
        ordem = 0
        x = ''
        y = ''
        orig = ''
        dest = ''
        p_x = 0.0
        p_y = 0.0
        
        #Lê o arquivo e armazena na forma lista de lista de tuplas
        #Formato de cada linha: [(p1_x,p1_y);(p2_x, p2_y);...;(pn_x,pn_y)]
        for line in self.__file:
            lista = []
            for c in line:
                if c == '(' or c == '[' or c == ']' or c == ';' or c == ' ':
                    continue
                elif c == ',':
                    if(len(x) == 0):
                        continue
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

    def verify(self, x, y, string):
        #print('stirng:',string)
        #print('caminho armazenado:', self.__pathway)
        if 'first' in string:
            #print('entrou')
            self.__pathway = []
            self.__possibilidades = []
            for path in self.__secure:
                d1 = self.dist(x, y, path[0][0], path[0][1])
                d2 = self.dist(path[0][0], path[0][1], path[1][0], path[1][1])
                #print('d1:',d1," d2:",d2)
                if d1 <= d2:
                    self.__possibilidades.append(path)
            if len(self.__possibilidades) == 0:
                #print('false')
                self.__pathway.append((x,y))
                return False
            else:
                return True
    
        elif string == 'normal':
            self.__pathway.append((x,y))
            for path in self.__possibilidades:
                #sliding window
                for i in range(1,len(path)-1):
                    r1 = self.dist(path[i-1][0], path[i-1][1], path[i][0], path[i][1])
                    r2 = self.dist(path[i][0], path[i][1], path[i+1][0], path[i+1][1])
                    d = self.dist(x, y, path[i][0], path[i][1])
                    #print('i: ',i,' r1:',r1,' r2:',r2,' d:',d)
                    if(d <= r1 or d <= r2):
                        return True
                if len(self.__possibilidades) > 1:
                    self.__possibilidades.remove(path)
            return False

    def salvar_caminho(self):
        print("\n\t--------- Salvando caminho em arquivo ---------")
        self.__secure.append(self.__pathway)
        p = self.__pathway
        string = str(p)
        self.__file = open(self.__filename, 'a')
        self.__file.write(string)
    
    def dist(self, x, y, w, z):
        d = math.sqrt(math.pow(x-w, 2) + math.pow(y-z, 2))
        return d