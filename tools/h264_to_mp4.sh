#!/bin/sh

while :
do
	FILES=`ls -l /home/cfcv/Desktop/Stream | awk '{print $9}' | sort -u`
    sleep 5
	for FILE in $FILES
	do
		echo "Converting file: $FILE..."
		ffmpeg -n -i /home/cfcv/Desktop/Stream/$FILE /home/cfcv/Desktop/git/ESS/front_end/assets/videos/$FILE.mp4 -hide_banner
        rm /home/cfcv/Desktop/Stream/$FILE
    done
done