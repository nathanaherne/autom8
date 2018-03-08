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
globalVars.dawn = sun['dawn'].replace(tzinfo=None)
globalVars.sunrise = sun['sunrise'].replace(tzinfo=None)
globalVars.noon = sun['noon'].replace(tzinfo=None)
globalVars.sunset = sun['sunset'].replace(tzinfo=None)
globalVars.dusk = sun['dusk'].replace(tzinfo=None)

print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))

#sun = city.sun( local=True)
print('Dawn UTC:    %s' % str(sun['dawn']))
#print('Dawn Local:    %s' % sun['dawn'].replace(tzinfo=pytz.timezone(globalVars.timezone)))
print('Sunrise UTC: %s' % str(sun['sunrise']))
#print('Sunrise Local: %s' % str(sun['sunrise']))
print('Noon UTC:    %s' % str(sun['noon']))
#print('Noon Local:    %s' % str(sun['noon']))
print('Sunset UTC:  %s' % str(sun['sunset']))
#print('Sunset Local:  %s' % str(sun['sunset']))
print('Dusk UTC:    %s' % str(sun['dusk']))
#print('Dusk Local:    %s' % str(sun['dusk']))
