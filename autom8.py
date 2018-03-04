#!/usr/bin/python

# Libraries
import RPi.GPIO as GPIO
import time
import pytz
from datetime import datetime, timedelta

GPIO.setmode(GPIO.BCM)

# Import program variables
import autom8_vars

# Import user variables
import autom8_userVars

##########################################################
# SETUP
# Set all pins to output and turn them off

for i in autom8_vars.outPins: 

        GPIO.setup(i, GPIO.OUT) 
        GPIO.output(i, 1)

# Get Sun stages
import autom8_sunMoon

#print('TESTING City: %s' % autom8_userVars.city)
#print('TESTING latitude: %s' % autom8_vars.locationLat)
#print('TESTING Longitude: %s' % autom8_vars.locationLon)

# Get current datetime NOW
#tz = pytz.timezone(autom8_userVars.country + "/" + autom8_userVars.city)
#print('TESTING Timezone: %s' % tz)
#datetimeNow = datetime.now(tz)
#print('TESTING Time now: %s' % datetimeNow)

#print('TESTING dawn: %s' % autom8_vars.dawn)

# calculate on/off times 
#dawnDiff = datetimeNow - autom8_vars.dawn
#print('TESTING time since dawn %s' % dawnDiff)

#dawnDiff = autom8_vars.dawn + timedelta(minutes=600)
#print('TESTING dawn +10h %s' % dawnDiff)

#print('TESTING PinArray %s' % autom8_userVars.funcOnOffArray)

import autom8_calcTimes

# if datetime is larger than sunrise then update sunrise

# if datetime is larger than sunset then update sunset

# calculate on/off times for each
