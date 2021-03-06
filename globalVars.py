#!/usr/bin/python

import datetime

# Variables for Autom8

# Location
locationLat = 0
locationLon = 0
timeZone = 0

# Relay to pin mapping
relay1Pin = 0
relay2Pin = 1
relay3Pin = 4
relay4Pin = 17
relay5Pin = 21
relay6Pin = 22
relay7Pin = 10
relay8Pin = 9

outPins = [relay1Pin, relay2Pin, relay3Pin, relay4Pin, relay5Pin, relay6Pin, relay7Pin, relay8Pin]

# Time variables
sunrise = datetime.datetime.now()
sunset = datetime.datetime.now()
noon = datetime.datetime.now()
dawn = datetime.datetime.now()
dusk = datetime.datetime.now()

