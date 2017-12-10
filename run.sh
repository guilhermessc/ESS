#!/bin/sh

# DEMO:

touch stream_log
touch take_video_log

cd src/comm/
./stream.sh >> stream_log &
cd ../../

./src/hal/drivers/camera/take_Video.py >> take_video_log &

