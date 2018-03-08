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
print('Dawn UTC:    %s' % str(globalVars.dawn))
print('Dawn Local:    %s' % str(globalVars.dawn.astimezone(globalVars.timezone)))
print('Sunrise UTC: %s' % str(globalVars.sunrise))
print('Sunrise Local:    %s' % str(globalVars.sunrise.astimezone(globalVars.timezone)))
print('Noon UTC:    %s' % str(globalVars.noon))
print('Noon Local:    %s' % str(globalVars.noon.astimezone(globalVars.timezone)))
print('Sunset UTC:  %s' % str(globalVars.sunset))
print('Subset Local:    %s' % str(globalVars.sunset.astimezone(globalVars.timezone)))
print('Dusk UTC:    %s' % str(globalVars.dusk))
print('Dusk Local:    %s' % str(globalVars.dusk.astimezone(globalVars.timezone)))
