#!/usr/bin/python

import datetime as dt

from datetime import timedelta, datetime

import autom8_userVars

import autom8_vars

# Loop through each Function OnOff setting
for funcN_Array in autom8_userVars.funcArray:

    # Check if functionOnOff value has plus or minus in them
    plus = funcN_Array[1].find("+")
    minus = funcN_Array[1].find("-")

    # If there is no time settings
    if funcN_Array[1] == "":
        startTime = "Blank"
        endTime = "Blank"

    # If function has been set to off
    elif funcN_Array[1] == "off":
        startTime = "Blank"
        endTime = "Blank"

    # If function is set to run always
    elif funcN_Array[1] == "always":
        startTime = datetime.now()
        endTime = "never"

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



    # Calculate Start Times
    if startTime == "dawn":
        funcN_Array[2] = autom8_vars.dawn
    elif startTime == "sunrise":
        funcN_Array[2] = autom8_vars.sunrise
    elif startTime == "noon":
        funcN_Array[2] = autom8_vars.noon
    elif startTime == "sunset":
        funcN_Array[2] = autom8_vars.sunset
    elif startTime == "dusk":
        funcN_Array[2] = autom8_vars.dawn
    elif isinstance(startTime, dt.datetime):
        funcN_Array[2] = startTime
    else:
        # Get hours/minutes 
        if startTime.find("h") != -1:
            hours = startTime.split("h")
            startTime = endTime - timedelta(hours=int(hours[0]))

        elif startTime.find("m") != -1:
            minutes = startTime.split("m")
            startTime = endTime - timedelta(minutes=int(minutes[0]))


    # Calculate End Times
    if endTime == "dawn":
        funcN_Array[3] = autom8_vars.dawn
    elif endTime == "sunrise":
        funcN_Array[3] = autom8_vars.sunrise
    elif endTime == "noon":
        funcN_Array[3] = autom8_vars.noon
    elif endTime == "sunset":
        funcN_Array[3] = autom8_vars.sunset
    elif endTime == "dusk":
        funcN_Array[3] = autom8_vars.dawn
    elif isinstance(endTime, dt.datetime):
        funcN_Array[3] = endTime
    else:
        # Get hours/minutes 
        if endTime.find("h") != -1:
            hours = endTime.split("h")
            endTime = startTime + timedelta(hours=int(hours[0]))

        elif endTime.find("m") != -1:
            minutes = endTime.split("m")
            endTime = startTime + timedelta(minutes=int(minutes[0]))


    print("TESTING funcX_Alias: ", funcN_Array[0])
    print("TESTING funcX_OnOff: ", funcN_Array[1])
    print("Start Time: ", str(funcN_Array[2]), "End Time: ", str(funcN_Array[3]))
    print("--------------------------------------------------")


