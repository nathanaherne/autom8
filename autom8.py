#!/usr/bin/python

# Libraries
import RPi.GPIO as GPIO
import time
import pytz
from datetime import datetime, timedelta

GPIO.setmode(GPIO.BCM)

# Import program variables
import globalVars

# Import user variables
import userVars

##########################################################
# SETUP
# Set all pins to output and turn them off

for i in globalVars.outPins: 

        GPIO.setup(i, GPIO.OUT) 
        GPIO.output(i, 1)

# Get Sun/Moon stages
import getSunMoon

# Calculate on/off times
import calcOnOff

# Set on/off times
import setOnOff
