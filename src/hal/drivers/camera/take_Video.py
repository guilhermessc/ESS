#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (620,480)
camera.framerate = 30
camera.start_preview()

camera.start_recording('../../../comm/to_stream/video000001.h264')
camera.wait_recording(5)

for i in range (2,86400):
    camera.split_recording('../../../comm/to_stream/video%06d.h264' % i)
    camera.wait_recording(5)

camera.stop_recording()

camera.stop_preview()
