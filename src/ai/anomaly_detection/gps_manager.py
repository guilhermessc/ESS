#TODO: handling exceptions
import time
#from gps import GPS
from secure_path import SP
from secure_area import SA

#Instance of the GPS emulator
#GPS = GPS()

#Instance of the secure area veryfier
SA = SA('Files/SafeSpaces.txt')

#Debug: show safe areas
SA.show_areas()

#Instance of the secure path veryfier
SP = SP('Files/SafePaths.txt')

#Debug: show safe paths
SP.show_paths()

secure_place_before = ''
secure_place_now = ''
status = ''

while True:
    (x,y) = GPS.get_location()

    secure_place_before = secure_place_now
    (b, secure_place_now) = SA.verify(x,y)
    if b:    
        status = 'Safe Area: '+secure_place_now
        continue
    else:
        (b, dest) = SP.verify(secure_place_before, x,y)
        if b:
            status = 'Safe Path: '+secure_place_before+'-'+dest
            continue
        else:
            status = 'Anomaly'
    print(status)

    #espera 1 segundo
    time.sleep(1)
    


