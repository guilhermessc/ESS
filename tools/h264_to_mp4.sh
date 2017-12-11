#!/bin/sh

while :
do
	FILES=`ls -l /home/cfcv/Desktop/Stream | awk '{print $9}' | sort -u`
    delay 3
	for FILE in $FILES
	do

		echo "Converting file: $FILE..."
		ffmpeg -i /home/cfcv/Desktop/Stream/$FILE /home/cfcv/Desktop/git/ESS/front_end/assets/videos/$FILE.mp4 -hide_banner
        delay 2
        rm /home/cfcv/Desktop/Stream/$FILE
    done
done