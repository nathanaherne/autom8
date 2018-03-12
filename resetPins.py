#!/usr/bin/python

# Libraries
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Import program variables
import globalVars

##########################################################
# SETUP
# Set all pins to output and turn them off

for i in globalVars.outPins: 

        GPIO.setup(i, GPIO.OUT) 
        GPIO.output(i, 1)
