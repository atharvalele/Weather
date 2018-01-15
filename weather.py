# Pull data from openweathermap.org
# Atharva Lele - 2018

import pyowm
import string   # for capwords()

# API Keys
owm = pyowm.OWM('b7686ed6ad45471e6ed20e35f9f860c1')

# Setting current location
print('\nEnter location: ', end='')
location = input()
current_location = owm.weather_at_place(location)
w = current_location.get_weather()

# Weather Details
temps = w.get_temperature('celsius')
wind = w.get_wind()
humidity = w.get_humidity()

# Outputting to console
#print(location)
print(string.capwords(w.get_detailed_status()))
print('\nCurrent: ' + str(temps['temp']) + 'C' + '\nMax: ' + str(temps['temp_max']) + 'C' +
        '\nMin: ' + str(temps['temp_min']) + 'C')
print('\nWind: ' + str((wind['speed'] * 3.6)) + ' km/h')
print('\nHumidity: ' + str(humidity) + '%\n')
