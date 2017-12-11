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
c_str = ''
flag = ''
msg = ''
print('\n--------------------------------\n')

while (not (servidor.wait_connection())):
    pass

while True:
    data = servidor.receive(1024)
    data_str = data.decode()
    print('coordenadas recebidas: ', data_str)
    x_str = ''
    y_str = ''
    ordem = 0
    for c in data_str:
        if c == ',':
            ordem += 1
            continue
        if ordem%2 == 0:
            x_str += c
        else:
            y_str += c
    
    try:
        x = float(x_str)
        y = float(y_str)
    except ValueError:
        print('Valor não faz sentido, ignorado!')
        continue

    print('\nCoordenada: ', x, ", ", y)
    #print('x: ',x, ' y: ',y)
    if SA.verify(x,y):
        msg = 'Nothing Important'
        if flag == 'Unusual':
            choice = input('\n\t\tNOTIFICAÇÃO: Seu filho(a) percorreu um caminho diferente\n\t\tDeseja salvar este novo caminho?[y/n]')
            msg = 'NOTIFICACAO: Seu filho(a) percorreu um caminho diferente, deseja salvar este caminho?'
            if choice == 'y':
                msg = 'Parabens voce cadastrou um novo caminho'
                print('entrou ')
                SP.salvar_caminho()
            flag = ''
        status = 'Safe Area'
        c_str = ''
        SP.erase_path()
    else:
        if c_str == 'first time':
            c_str = 'normal'
        
        if c_str == '':
            c_str = 'first time'

        if SP.verify(x,y,c_str):
            status = 'Safe Path'
            c_str = 'normal'
        else:
            if(not (status == 'Anomaly')):
                print('\n\t\t---------------------------')
                print('\t\t--- ROTA ESTRANHA!!!!!! ---')
                print('\t\t---------------------------')
                msg = 'Rota estranha!'
                flag = 'Unusual'
            status = 'Anomaly'

    print('-> Status: ',status,'\n')
    print('msg:', msg)
    #json
    j = {
        'status': status,
        'message': msg,
        'coord_y': y,    
        'coord_x': x
    }
    f = open('../../../front_end/_site/assets/gps/gps.json', 'w')
    json.dump(j, f)
    f.close()
    #espera 1 segundo
#    time.sleep(1)
    
