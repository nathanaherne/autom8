#!/usr/bin/python

import globalVars
import userVars

from datetime import datetime
import RPi.GPIO as GPIO
import pytz

# Get current time.

# Loop through each Function OnOff setting
for funcN_Array, i in zip(userVars.funcArray, globalVars.outPins):

	print("--------------------------------------------------")
	print(str(funcN_Array[0]), "On/Off setting is: ", funcN_Array[1])

	# If startTime is less than now() and startTime is not blank AND
	# endTime > now() OR endTime is blank
	if funcN_Array[2] != datetime.min:

		if funcN_Array[2] <= datetime.utcnow() and (funcN_Array[3] > datetime.utcnow() or funcN_Array[3] == datetime.max) :
			# Turn pin on
			GPIO.output(i, 0)
			print("Currently on - turned on at", str(funcN_Array[2]))
			print("Will turn off at", str(funcN_Array[3]))
		else:
			# Turn pin off
			GPIO.output(i, 1)
			print("Turned off at", str(funcN_Array[3]))