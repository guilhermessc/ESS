#!/usr/bin/env python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (620,480)
camera.framerate = 30
camera.start_preview()
i = 1
camera.start_recording('/../../comm/to_stream/%010d.h264' % i)
camera.wait_recording(1)

for i in range (2,86400):
    camera.split_recording('/../../comm/to_stream/%010d.h264' % i)
    camera.wait_recording(1)

camera.stop_recording()

camera.stop_preview()
