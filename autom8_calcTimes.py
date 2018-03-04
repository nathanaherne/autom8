#!/usr/bin/python

import autom8_userVars

# Loop through each Function OnOff setting
for funcSettings in autom8_userVars.funcOnOffArray:
    print("TESTING funcSettings: ", funcSettings)

    # Check if functionOnOff value has plus or minus in them
    plus = funcSettings.find("+")
    print("TESTING Plus: ", plus)
    minus = funcSettings.find("-")
    print("TESTING Minus: ", minus) 

    # If there is no time settings
    if funcSettings == "":
        startTime = "Blank"
        endTime = "Blank"
        print("Start Time: ", startTime, "End Time: " endtime)

    # If function has been set to off
    elif funcSettings == "off":
        startTime = "Blank"
        endTime = "Blank"
        print("Start Time: ", startTime, "End Time: " endtime)

    # If function is set to run always
    elif funcSettings == "always":
        startTime = "now"
        endTime = "now + 12 hours"
        print("Start Time: ", startTime, "End Time: " endtime)

    # If function has "+" or "-" in its timesetting
    elif plus:
        beforeAfterOperand = funcSettings.split("+")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]
        print("Start Time: ", startTime, "End Time: " endtime)
        
    elif minus:
        beforeAfterOperand = funcSettings.split("+")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]
        print("Start Time: ", startTime, "End Time: " endtime)

    else:
        print("ERROR")


