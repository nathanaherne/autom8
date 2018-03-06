#!/usr/bin/python

import globalVars
import userVars

from datetime import datetime

# Get current time.

# Loop through each Function OnOff setting
for funcN_Array, i in zip(userVars.funcArray, globalVars.outPins):

	# If startTime is less than now() and startTime is not blank AND
	# endTime > now() OR endTime is blank
	if (funcN_Array[2] <= datetime.now() and funcN_Array[2] != "") and (funcN_Array[3] > datetime.now() or funcN_Array[3] == ""):

		# Turn pin on
		GPIO.output(i, 0)
	else:
		# Turn pin off
		GPIO.output(i, 1)