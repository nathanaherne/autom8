#!/usr/bin/python

import datetime
from astral import Astral
import pytz

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
print('Dawn UTC:    %s' % str(sun['dawn']))
print('Dawn Local:    %s' % sun['dawn'].replace(tzinfo=pytz.timezone(globalVars.timezone)))
print('Sunrise UTC: %s' % str(sun['sunrise']))
print('Sunrise Local: %s' % str(sun['sunrise']))
print('Noon Local:    %s' % str(sun['noon']))
print('Sunset Local:  %s' % str(sun['sunset']))
print('Dusk Local:    %s' % str(sun['dusk']))
