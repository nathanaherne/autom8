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

globalVars.timezone = city.timezone
globalVars.locationLat = city.latitude
globalVars.locationLon = city.longitude

sun = city.sun(local=False)
globalVars.dawn = sun['dawn'].replace(tzinfo=None)
globalVars.sunrise = sun['sunrise'].replace(tzinfo=None)
globalVars.noon = sun['noon'].replace(tzinfo=None)
globalVars.sunset = sun['sunset'].replace(tzinfo=None)
globalVars.dusk = sun['dusk'].replace(tzinfo=None)

print('Sun Information for %s/%s' % (userVars.city, city.region))
print('Timezone: %s' % globalVars.timezone)
print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))
print('---------------------------------------------------')
print('Dawn Local:		%s' % str(globalVars.dawn.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(globalVars.timezone))))
print('Sunrise Local:		%s' % str(globalVars.sunrise.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(globalVars.timezone))))
print('Noon Local:		%s' % str(globalVars.noon.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(globalVars.timezone))))
print('Sunset Local:		%s' % str(globalVars.sunset.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(globalVars.timezone))))
print('Dusk Local:		%s' % str(globalVars.dusk.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(globalVars.timezone))))
print('---------------------------------------------------')
print('Dawn UTC:    %s' % str(globalVars.dawn))
print('Sunrise UTC: %s' % str(globalVars.sunrise))
print('Noon UTC:    %s' % str(globalVars.noon))
print('Sunset UTC:  %s' % str(globalVars.sunset))
print('Dusk UTC:    %s' % str(globalVars.dusk))
