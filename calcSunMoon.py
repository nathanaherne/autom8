#!/usr/bin/python

import datetime
from astral import Astral

# Import autom8 variables
import globalVars
import userVars

a = Astral()
a.solar_depression = 'civil'

city = a[userVars.city]

print('Information for %s/%s\n' % (userVars.city, city.region))

globalVars.timezone = city.timezone
print('Timezone: %s' % globalVars.timezone)

globalVars.locationLat = city.latitude
globalVars.locationLon = city.longitude

sun = city.sun(local=False)
globalVars.dawn = sun['dawn']
globalVars.sunrise = sun['sunrise']
globalVars.noon = sun['noon']
globalVars.sunset = sun['sunset']
globalVars.dusk = sun['dusk']

print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))

#sun = city.sun( local=True)
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Noon:    %s' % str(sun['noon']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))
