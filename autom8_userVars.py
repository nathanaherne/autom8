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
func1_OnOff = "always"
func1_On = "now" # Calculated
func1_Off = "now" # Calculated
func1_Array = [func1_Alias, func1_OnOff, func1_On, func1_Off]

func2_Alias = "Pond Lights"
func2_OnOff = "sunset+5h"
func2_On = "now" # Calculated
func2_Off = "now" # Calculated
func1_Array = [func2_Alias, func2_OnOff, func2_On, func2_Off]

func3_Alias = "Side Lights"
func3_OnOff = "sunset+5h"
func3_On = "now" # Calculated
func3_Off = "now" # Calculated
func3_Array = [func3_Alias, func3_OnOff, func3_On, func3_Off]

func4_Alias = "Cubby House"
func4_OnOff = "sunset+5h"
func4_On = "now" # Calculated
func4_Off = "now" # Calculated
func4_Array = [func4_Alias, func4_OnOff, func4_On, func4_Off]

func5_Alias = "Garden Irrigation"
func5_OnOff = "dawn-5m"
func5_On = "now" # Calculated
func5_Off = "now" # Calculated
func5_Array = [func5_Alias, func5_OnOff, func5_On, func5_Off]

func6_Alias = "Vege Gardens"
func6_OnOff = "dawn-5m"
func6_On = "now" # Calculated
func6_Off = "now" # Calculated
func6_Array = [func6_Alias, func6_OnOff, func6_On, func6_Off]

func7_Alias = ""
func7_OnOff = ""
func7_On = "now" # Calculated
func7_Off = "now" # Calculated
func7_Array = [func7_Alias, func7_OnOff, func7_On, func7_Off]

func8_Alias = ""
func8_OnOff = ""
func8_On = "now" # Calculated
func8_Off = "now" # Calculated
func8_Array = [func8_Alias, func8_OnOff, func8_On, func8_Off]

# Array of all function settings
funcArray = [func1_Array, func2_Array, func3_Array, func4_Array, func5_Array, func6_Array, func7_Array, func8_Array]

