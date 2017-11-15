#!/usr/bin/env python
import wiringpi

wiringpi.wiringPiSetup()

wiringpi.pinMode(5,1)
wiringpi.pinMode(4,0)


while True:
	wiringpi.digitalWrite(5,1)
	if wiringpi.digitalRead(4):
		print("1")
	else:
		print("0")