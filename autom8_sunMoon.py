#!/usr/bin/python

import datetime
from astral import Astral
#import datetime

# Import autom8 variables
import autom8_vars

# Import User Variables
import autom8_userVars

a = Astral()
a.solar_depression = 'civil'

city = a[autom8_userVars.city]

print('Information for %s/%s\n' % (autom8_userVars.city, city.region))

timezone = city.timezone
print('Timezone: %s' % timezone)

autom8_vars.locationLat = city.latitude
autom8_vars.locationLon = city.longitude

sun = city.sun(local=True)
autom8_vars.dawn = datetime.datetime(sun['dawn'])
autom8_vars.sunrise = sun['sunrise']
autom8_vars.noon = sun['noon']
autom8_vars.sunset = sun['sunset']
autom8_vars.dusk = sun['dusk']

print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))

#sun = city.sun( local=True)
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Noon:    %s' % str(sun['noon']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))
