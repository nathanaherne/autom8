#!/usr/bin/python

import autom8_userVars

# Loop through each Function OnOff setting
for i in autom8_userVars.funcOnOffArray:
    print("TESTING i: ", i)

    # Check if functionOnOff value has plus or minus in them
    plus = i.find("+")
    print("TESTING Plus: ", plus)
    minus = i.find("-")
    print("TESTING Minus: ", minus) 

    # If there is no time settings
    if timeSetting == "":
        startTime = ""
        endTime = ""

    # If function has been set to off
    elif timeSetting == "off":
        startTime = ""
        endTime = ""

    # If function is set to run always
    elif timeSetting == "always":
        startTime = "now"
        endTime = "now + 12 hours"

    # If function has "+" or "-" in its timesetting
    elif plus:
        beforeAfterPlus = i.split("+")
        print("TESTING beforePlus ", beforeAfterPlus[0], " AfterPlus ", beforeAfterPlus[1])
        #startTime = "before+"
        #endTime = "before+" + "after +"
        
    elif minus:
        beforeAfterMinus = i.split("+")
        print("TESTING beforeMinux ", beforeAfterMinus[0], " AfterMinus ", beforeAfterMinus[1])
        #startTime = "before-" - "after-"
        #endTime = "before-"

    else:
        print("ERROR")


