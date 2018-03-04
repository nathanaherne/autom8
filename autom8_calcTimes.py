#!/usr/bin/python

import autom8_userVars

# Loop through each Function OnOff setting
for i in funcOnOffArray:
    print("TESTING i: ", i)

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
    else:
        plus = i.find("+")
        print("TESTING Plus: ", plus)
        minus = i.find("-")
        print("TESTING Minus: ", minus) 

        # If Plus "+"
        if plus:
            beforeAfterPlus = i.split("+")
            print("TESTING beforePlus ", beforeAfterPlus[0], " AfterPlus ", beforeAfterPlus[1])
            #startTime = "before+"
            #endTime = "before+" + "after +"
        
        elif minus:
            #startTime = "before-" - "after-"
            #endTime = "before-"

        else:
            print("ERROR")


