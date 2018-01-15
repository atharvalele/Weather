# Pull data from openweathermap.org
# Atharva Lele - 2018

import pyowm
import string   # for capwords()

# API Key
api_key = # your api key
owm = pyowm.OWM(api_key)

# Setting current location
print('\nEnter location: ', end='')
location = input()
try:
        current_location = owm.weather_at_place(location)
except:
        print("Cannot find location")
        exit()
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
print('Humidity: ' + str(humidity) + '%\n')

# 7 day forecast
fc = owm.daily_forecast(location, limit = 7)
f = fc.get_forecast()
for day in f:
        print(day.get_reference_time('iso')[:10] + ' ' + string.capwords(day.get_detailed_status()))