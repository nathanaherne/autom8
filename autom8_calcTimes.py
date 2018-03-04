#!/usr/bin/python

import autom8_userVars

# Loop through each Function OnOff setting
for funcOnOff in autom8_userVars.funcOnOffArray:

    # Check if functionOnOff value has plus or minus in them
    plus = funcOnOff.find("+")
    minus = funcOnOff.find("-")

    # If there is no time settings
    if funcOnOff == "":
        startTime = "Blank"
        endTime = "Blank"

    # If function has been set to off
    elif funcOnOff == "off":
        startTime = "Blank"
        endTime = "Blank"

    # If function is set to run always
    elif funcOnOff == "always":
        startTime = "now"
        endTime = "never"

    # If functionOnOff has "+"
    elif plus != -1:
        beforeAfterOperand = funcOnOff.split("+")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]
        
    elif minus != -1:
        beforeAfterOperand = funcOnOff.split("-")
        startTime = beforeAfterOperand[0]
        endTime = beforeAfterOperand[1]

    else:
        print("ERROR")

print("TESTING funcOnOff: ", funcOnOff)
if plus != -1:
    print("Plus Found: ", plus)
elif minus != -1:
    print("Minus Found: ", minus)

print("Start Time: ", startTime, "End Time: ", endTime)


