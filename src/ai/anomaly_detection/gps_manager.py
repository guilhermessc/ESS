#TODO: handling exceptions
import time
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
print('\n--------------------------------\n')

while (not (servidor.wait_connection())):
    pass

while True:
    data = sock.receive(1024)
    print('coordenadas recebidas: ', data)
   
#    if SA.verify(x,y):
#        if flag == 'Unusual':
#            choice = input('\n\t\tNOTIFICAÇÃO: Seu filho(a) percorreu um caminho diferente\n\t\tDeseja salvar este novo caminho?[y/n]')
#            if choice == 'y':
#                print('entrou ')
#                SP.salvar_caminho()
#            flag = ''
#        status = 'Safe Area'
#        c = ''
#    else:
#        if c == 'first time':
#            c = 'normal'
#        
#        if c == '':
#            c = 'first time'
#
#        if SP.verify(x,y,c):
#            status = 'Safe Path'
#            c = 'normal'
#        else:
#            if(not (status == 'Anomaly')):
#                print('\n\t\t---------------------------')
#                print('\t\t--- ROTA ESTRANHA!!!!!! ---')
#                print('\t\t---------------------------')
#                flag = 'Unusual'
#            status = 'Anomaly'

#    print('\nCoordenada: ', x, ", ",y)
#    print('-> Status: ',status,'\n')
    #espera 1 segundo
#    time.sleep(1)
    
