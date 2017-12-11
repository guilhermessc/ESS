#!/bin/sh

# DEMO:

touch stream_log
touch take_video_log
touch gps_driver_log

cd src/comm/
./stream.sh > ../../stream_log &
cd ../../

cd src/hal/drivers/camera/
./take_Video.py > ../../../../take_video_log &
cd ../../../../


# the gps driver is a simulation on the keyboard
cd src/hal/drivers/
./gps.py

