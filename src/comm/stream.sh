#!/bin/sh

# TODO: Update parameter passing
PWRD=raspberry
LOCAL=cfcv@192.168.15.9
REMOTE_PATH=/home/cfcv/Desktop/Stream/
TO_STREAM=to_stream/

while :
do
	FILES=`ls -l $TO_STREAM | awk '{print $9}' | sort -u`

	for FILE in $FILES
	do

		echo "Sending file: $FILE..."
		sshpass -p "$PWRD" scp $TO_STREAM/$FILE $LOCAL:$REMOTE_PATH
		RETVAL=$?
		if [ $RETVAL -eq 0 ] ; then
			rm $TO_STREAM/$FILE
		fi
	done
done
