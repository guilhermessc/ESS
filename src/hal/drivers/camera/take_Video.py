#!/usr/bin/env python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (620,480)
camera.framerate = 10
camera.start_preview()

camera.start_recording('/home/pi/Desktop/ESS/src/comm/to_stream/video1.h264')
camera.wait_recording(1)

for i in range (2,86400):
    camera.split_recording('/home/pi/Desktop/ESS/src/comm/to_stream/video%d.h264' % i)
    camera.wait_recording(1)

camera.stop_recording()

camera.stop_preview()
