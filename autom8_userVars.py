#!/usr/bin/python

# USER VARIABLES

# Location
country = "Australia"
city = "Brisbane"

# Function on/off settings
# always = always on, no value = always off, now = on now, off = off now
# sunset+10h = turn on at sunset for 10 hours
# sunset-5m = turn on 5 minutes before sunset and turn off at sunset
# sunrise+5h = turn on at sunrise for 5 hours
# sunrise-7 = turn on 7 minutes before sunrise
# dawn+5h = turn on at dawn for 5 hours and turn off at dawn
# noon = when sun is highest in sky

# Array is [start_datetime(required), end_datetime(optional), frequency(optional), exception(optional), script(optional))

func1_Alias = "Pond Pump"
func2_Alias = "Pond Lights"
func3_Alias = "Side Lights"
func4_Alias = "Cubby House"
func5_Alias = "Garden Irrigation"
func6_Alias = "Vege Gardens"
func7_Alias = ""
func8_Alias = ""

func1_OnOff = "always"
func2_OnOff = "sunset+5h"
func3_OnOff = "sunset+5h"
func4_OnOff = "sunset+5h"
func5_OnOff = "dawn-5m"
func6_OnOff = "dawn-5m"
func7_OnOff = ""
func8_OnOff = ""

funcOnOffArray = [func1_OnOff, func2_OnOff, func3_OnOff, func4_OnOff, func5_OnOff, func6_OnOff, func7_OnOff, func8_OnOff]

# Calculated On Times
func1_On = "now"
func2_On = "sunset"
func3_On = "sunset"
func4_On = "sunset"
func5_On = "dawn"
func6_On = "dawn"
func7_On = ""
func8_On = ""

# Calculated Off Times
func1_Off = ""
func2_Off = "sunset+5h"
func3_Off = "sunset+5h"
func4_Off = "sunset+5h"
func5_Off = ""
func6_Off = ""
func7_Off = ""
func8_Off = ""
