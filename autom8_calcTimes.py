#!/usr/bin/python

import autom8_userVars

# Loop through each Function OnOff setting
for funcN_Array in autom8_userVars.funcArray:

    # Check if functionOnOff value has plus or minus in them
    plus = funcN_Array[1].find("+")
    minus = funcN_Array[1].find("-")

    # If there is no time settings
    if funcN_Array[1] == "":
        funcN_Array[2] = "Blank"
        funcN_Array[3] = "Blank"

    # If function has been set to off
    elif funcN_Array[1] == "off":
        funcN_Array[2] = "Blank"
        funcN_Array[3] = "Blank"

    # If function is set to run always
    elif funcN_Array[1] == "always":
        funcN_Array[2] = "now"
        funcN_Array[3] = "never"

    # If functionOnOff has "+"
    elif plus != -1:
        beforeAfterOperand = funcN_Array[1].split("+")
        funcN_Array[2] = beforeAfterOperand[0]
        funcN_Array[3] = beforeAfterOperand[1]
        
    elif minus != -1:
        beforeAfterOperand = funcN_Array[1].split("-")
        funcN_Array[2] = beforeAfterOperand[1]
        funcN_Array[3] = beforeAfterOperand[0]

    else:
        print("ERROR")

    print("TESTING funcX_Alias: ", funcN_Array[0])
    print("TESTING funcX_OnOff: ", funcN_Array[1])
    print("Start Time: ", funcN_Array[2], "End Time: ", funcN_Array[3])
    print("--------------------------------------------------")


