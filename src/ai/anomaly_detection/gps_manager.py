#TODO: handling exceptions
import time
import json
from Server import Server
from secure_path import SP
from secure_area import SA

#Insance of socket
servidor = Server(7000)

#Instance of the secure area veryfier
SA = SA('Files/SafeSpaces.txt')

#Debug: show safe areas
SA.show_areas()

#Instance of the secure path veryfier
SP = SP('Files/SafePaths.txt')

#Debug: show safe paths
SP.show_paths()

status = ''
c = ''
flag = ''
msg = ''
print('\n--------------------------------\n')

while (not (servidor.wait_connection())):
    pass

while True:
    data = servidor.receive(1024)
    data_str = data.decode()
    #print('coordenadas recebidas: ', data_str)
    x_str = ''
    y_str = ''
    msg = ''
    ordem = 0
    for c in data_str:
        if c == ',':
            ordem += 1
            continue
        if ordem%2 == 0:
            x_str += c
        else:
            y_str += c
    
    x = float(x_str)
    y = float(y_str)
    #print('x: ',x, ' y: ',y)
    if SA.verify(x,y):
        if flag == 'Unusual':
            choice = input('\n\t\tNOTIFICAÇÃO: Seu filho(a) percorreu um caminho diferente\n\t\tDeseja salvar este novo caminho?[y/n]')
            msg = 'NOTIFICAÇÃO: Seu filho(a) percorreu um caminho diferente, deseja salvar este caminho?'
            if choice == 'y':
                print('entrou ')
                SP.salvar_caminho()
            flag = ''
        status = 'Safe Area'
        c = ''
    else:
        if c == 'first time':
            c = 'normal'
        
        if c == '':
            c = 'first time'

        if SP.verify(x,y,c):
            status = 'Safe Path'
            c = 'normal'
        else:
            if(not (status == 'Anomaly')):
                print('\n\t\t---------------------------')
                print('\t\t--- ROTA ESTRANHA!!!!!! ---')
                print('\t\t---------------------------')
                msg = 'Rota estranha!'
                flag = 'Unusual'
            status = 'Anomaly'

    print('\nCoordenada: ', x, ", ",y)
    print('-> Status: ',status,'\n')
    #json
    j = {
        'status': status,
        'message': msg,
        'coord_y': y    
        'coord_x': x,
    }
    with open('data.json', 'w') as f:
        j.dump(data, f)
    #espera 1 segundo
#    time.sleep(1)
    

