#!/usr/bin/python

import autom8_userVars

# Loop through each Function OnOff setting
for funcSettings in autom8_userVars.funcOnOffArray:

    # Check if functionOnOff value has plus or minus in them
    plus = funcSettings.find("+")
    minus = funcSettings.find("-")

    # If there is no time settings
    if funcSettings == "":
        startTime = "Blank"
        endTime = "Blank"

    # If function has been set to off
    elif funcSettings == "off":
        startTime = "Blank"
        endTime = "Blank"

    # If function is set to run always
    elif funcSettings == "always":
        startTime = "now"
        endTime = "never"

    # If function has "+" or "-" in its timesetting
    elif plus:
        beforeAfterOperand = funcSettings.split("+")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]
        
    elif minus:
        beforeAfterOperand = funcSettings.split("+")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]

    else:
        print("ERROR")
`   
    print("TESTING funcSettings: ", funcSettings)
    if plus:
        print("Plus Found: ", plus)
    elif minus;
    print("Minus Found: ", minus)

    print("Start Time: ", startTime, "End Time: ", endTime)


