#!/usr/bin/python

import datetime as dt

from datetime import timedelta, datetime

import userVars

import globalVars

# Loop through each Function OnOff setting
for funcN_Array in userVars.funcArray:

    # Check if functionOnOff value has plus or minus in them
    plus = funcN_Array[1].find("+")
    minus = funcN_Array[1].find("-")

    # If there is no time settings
    if funcN_Array[1] == "":
        startTime = datetime.min
        endTime = datetime.min

    # If function has been set to off
    elif funcN_Array[1] == "off":
        startTime = datetime.min
        endTime = datetime.min

    # If function is set to run always
    elif funcN_Array[1] == "always":
        startTime = datetime.now()
        endTime = datetime.max

    # If functionOnOff has "+"
    elif plus != -1:
        beforeAfterOperand = funcN_Array[1].split("+")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]
        
    elif minus != -1:
        beforeAfterOperand = funcN_Array[1].split("-")
        startTime = beforeAfterOperand[1]
        endTime = beforeAfterOperand[0]

    else:
        print("ERROR")


    # Insert Start Times
    if startTime == "dawn":
        funcN_Array[2] = globalVars.dawn
    elif startTime == "sunrise":
        funcN_Array[2] = globalVars.sunrise
    elif startTime == "noon":
        funcN_Array[2] = globalVars.noon
    elif startTime == "sunset":
        funcN_Array[2] = globalVars.sunset
    elif startTime == "dusk":
        funcN_Array[2] = globalVars.dawn
    elif isinstance(startTime, dt.datetime):
        funcN_Array[2] = startTime


    # Insert End Times
    if endTime == "dawn":
        funcN_Array[3] = globalVars.dawn
    elif endTime == "sunrise":
        funcN_Array[3] = globalVars.sunrise
    elif endTime == "noon":
        funcN_Array[3] = globalVars.noon
    elif endTime == "sunset":
        funcN_Array[3] = globalVars.sunset
    elif endTime == "dusk":
        funcN_Array[3] = globalVars.dawn
    elif isinstance(endTime, dt.datetime):
        funcN_Array[3] = endTime


    # Calculate Start Times
    # If StartTime contains hours or minutes
    if isinstance(startTime, dt.datetime) == False and startTime.find("h") != -1:
        hours = startTime.split("h")
        funcN_Array[2] = funcN_Array[3] - timedelta(hours=int(hours[0]))

    elif isinstance(startTime, dt.datetime) == False and startTime.find("m") != -1:
        minutes = startTime.split("m")
        funcN_Array[2] = funcN_Array[3] - timedelta(minutes=int(minutes[0]))


    # Calculate End Times
    # If EndTime contains hours or minutes
    if isinstance(endTime, dt.datetime) == False and endTime.find("h") != -1:
        hours = endTime.split("h")
        funcN_Array[3] = funcN_Array[2] + timedelta(hours=int(hours[0]))

    elif isinstance(endTime, dt.datetime) == False and endTime.find("m") != -1:
        minutes = endTime.split("m")
        funcN_Array[3] = funcN_Array[2] + timedelta(minutes=int(minutes[0]))


    print("TESTING funcX_Alias: ", funcN_Array[0])
    print("TESTING funcX_OnOff: ", funcN_Array[1])
    print("Start Time: ", str(funcN_Array[2]), "End Time: ", str(funcN_Array[3]))
    print("--------------------------------------------------")


