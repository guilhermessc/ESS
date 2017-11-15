#! /bin/bash
for n in {1..100}; do
	sleep 1
	dd if=/dev/zero of=file$( printf %03d "$n" ).txt count=1024 bs=70
done
#for testing the connection, it generates files of size bs*count
