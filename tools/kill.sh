#!/bin/sh

STREAMD=`ps -a | grep stream.sh | awk '{print $1}'`
CAMERAD=`ps -a | grep python3 | awk '{print $1}'`

kill $STREAMD $CAMERAD
