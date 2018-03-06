#!/usr/bin/python

import globalVars
import userVars

from datetime import datetime
import RPi.GPIO as GPIO

# Get current time.

# Loop through each Function OnOff setting
for funcN_Array, i in zip(userVars.funcArray, globalVars.outPins):

	print("TESTING Function Name", funcN_Array[0])
	print("TESTING Function On/Off", funcN_Array[1])
	print("TESTING Function On", funcN_Array[2])
	print("TESTING Function Off", funcN_Array[3])

	# If startTime is less than now() and startTime is not blank AND
	# endTime > now() OR endTime is blank
	if funcN_Array[2] != datetime.min:

		if funcN_Array[2] <= datetime.now(utc) and (funcN_Array[3] > datetime.now(utc) or funcN_Array[3] == datetime.max):

			# Turn pin on
			GPIO.output(i, 0)
		else:
			# Turn pin off
			GPIO.output(i, 1)