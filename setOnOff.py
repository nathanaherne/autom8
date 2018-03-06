#!/usr/bin/python

import globalVars
import userVars

from datetime import datetime
import RPi.GPIO as GPIO

# Get current time.

# Loop through each Function OnOff setting
for funcN_Array, i in zip(userVars.funcArray, globalVars.outPins):

	print("TESTING Function Name", type(funcN_Array[0]))
	print("TESTING Function On/Off", type(funcN_Array[1]))
	print("TESTING Function On", type(funcN_Array[2]))
	print("TESTING Function Off", type(funcN_Array[3]))

	# If startTime is less than now() and startTime is not blank AND
	# endTime > now() OR endTime is blank
	if funcN_Array[2] != "":

		if funcN_Array[2] <= datetime.now() and (funcN_Array[3] > datetime.now() or funcN_Array[3] == ''):

			# Turn pin on
			GPIO.output(i, 0)
		else:
			# Turn pin off
			GPIO.output(i, 1)