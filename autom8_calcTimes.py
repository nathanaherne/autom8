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
        startTime = ""
        endTime = ""

    # If function has been set to off
    elif funcSettings == "off":
        startTime = ""
        endTime = ""

    # If function is set to run always
    elif funcSettings == "always":
        startTime = "now"
        endTime = "now + 12 hours"

    # If function has "+" or "-" in its timesetting
    elif plus:
        beforeAfterPlus = funcSettings.split("+")
        print("TESTING beforePlus ", beforeAfterPlus[0], " AfterPlus ", beforeAfterPlus[1])
        #startTime = "before+"
        #endTime = "before+" + "after +"
        
    elif minus:
        beforeAfterMinus = funcSettings.split("+")
        print("TESTING beforeMinux ", beforeAfterMinus[0], " AfterMinus ", beforeAfterMinus[1])
        #startTime = "before-" - "after-"
        #endTime = "before-"

    else:
        print("ERROR")


