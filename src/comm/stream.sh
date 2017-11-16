#!/bin/sh

# TODO: Update parameter passing
PWRD=raspberry
LOCAL=pi@192.168.25.9
REMOTE_PATH=/home/pi/Desktop/
TO_STREAM=to_stream/

while :
do
	FILES=`ls -l $TO_STREAM | awk '{print $9}' | sort -u`

	for FILE in $FILES
	do

		echo "Sending file: $FILE..."
		sshpass -p "$PWRD" scp $TO_STREAM/$FILE $LOCAL:$REMOTE_PATH
		# TODO: remove sent files
		rm $TO_STREAM/$FILE

	done
done