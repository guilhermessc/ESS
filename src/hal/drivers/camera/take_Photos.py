#!/usr/bin/env python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (620,480)

#alpha parameter
camera.start_preview()
for i in range (30):
    #sleep(0.0333)
    camera.capture('/home/pi/Desktop/photos_and_Videos2/image%s.jpg' % i)  

camera.stop_preview()

for filename in camera.record_sequence(
        '%d.h264' % i for i in range(1, 11)):
    camera.wait_recording(5)
