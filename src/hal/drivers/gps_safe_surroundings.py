#!/usr/bin/env python3
import sys
from socket import *
from math import sqrt


### Caso queira alterar essa porta lembre-se de altere tambem no client ###
PORT_TCP = 10003

sock = socket(AF_INET, SOCK_STREAM)
HOST = gethostbyname('0.0.0.0')
sock.bind( (HOST, PORT_TCP) )
sock.listen(1)

while True:
    print ('GPS disconnected!')
    connection, client_address = sock.accept()
    print ('Connection established.')
    while True:
        data = connection.recv(1024)
        str = data.decode('utf-8')

        #checking if we are receiving data from gps
        if data:
            print()
        else:
            print ('GPS lost.', client_address)
            break

        
        i = 0
        while str[i] != ',':
            i = i+1

        x = float(str[:i-1])
        y = float(str[i+1:])

        ############Code for Safe Surrounding here##########
        file = open('safeSpaces.txt', 'r+')
        for line in  file:
            #j holds the start of the string while i holds the last position of the string
            
            j = 1
            i = 0
            
            while line[i] != ',':
                i = i+1     

            x0 = float(line[j:i-1])            
            i = i+1
            j = i 

            while line[i] != ',':
                i = i+1
            
            y0 = float(line[j:i-1])
            i = i+1
            j = i

            while line[i] != ',':
                i = i+1
            x1 = float(line[j:i-1])
            i = i+1
            j = i
            
            while line[i] != ')':
                i = i+1
            y1 = float(line[j:i-1])

 #           print("x|y|x1|y1",x,y,x1,y1) 
            rDanger = sqrt((x-x0)**2+(y-y0)**2)
            rSafe = sqrt((x1-x0)**2+(y1-y0)**2)
#            print("rDanger|rSafe: ",rDanger,rSafe)
            
            if rSafe > rDanger:
                status = "Secure"
                break
            
            else:
                status = "Dangerous"
        ####################################################

        print(status)
        if status == "Dangerous":
            dangerFlag = True         
        
        if status == "Secure":
            dangerFlag = False

connection.close()