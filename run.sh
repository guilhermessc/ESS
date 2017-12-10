#!/bin/sh

# DEMO:

touch stream_log
touch take_video_log

./src/comm/stream.sh >> stream_log &
./src/hal/drivers/camera/take_Video.py >> take_video_log &

