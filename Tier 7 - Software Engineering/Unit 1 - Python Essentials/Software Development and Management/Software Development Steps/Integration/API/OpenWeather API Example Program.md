# **Example: OpenWeather API**
The following Python program open_weather.py uses the [OpenWeather API](https://www.openweathermap.org) to tell the user current weather information. 

The beauty of using this is that OpenWeather frequently update their data so you do not need to constantly be downloading datasets and reimporting them.

**However,** please note you **MUST** get your own **API_KEY** from the Open Weather Map website for this to work, and replace that in the code. 

**⚠️Unfortunately, since this program was written in 2024, the API has been subscription walled. Whilst most API calls are free, a subscription is now required :''(**

```python
import requests
import json

# API Key for OpenWeatherMap
# Please note: You must go to openweather map and get you own API key.
api_key = '' # <-- replace with your API key

# Function to get current weather conditions and 5-day forecast
def get_weather(location): 
    # API endpoint for current weather
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    # API endpoint for 5-day forecast
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'

    # Make GET request to API
    current_weather_response = requests.get(current_weather_url)
    forecast_response = requests.get(forecast_url)

    # Parse JSON response
    current_weather_data = json.loads(current_weather_response.text) # <-- convert JSON response to Python dictionary
    forecast_data = json.loads(forecast_response.text) # <-- convert JSON response to Python dictionary

    # Extract current weather conditions
    current_temp = current_weather_data['main']['temp'] # <-- extract temperature from dictionary
    current_weather = current_weather_data['weather'][0]['description'] # <-- extract weather description from dictionary

    # Extract forecast for next 5 days
    forecast_list = forecast_data['list'] # <-- extract list of forecasts from dictionary
    forecast = {} # <-- create empty dictionary to store forecast
    for f in forecast_list: # <-- loop through list of forecasts
        date = f['dt_txt'][:10] # <-- extract date from forecast
        if date not in forecast: # <-- check if date is already in forecast dictionary
            forecast[date] = { # 
                'temp': f['main']['temp'],
                'weather': f['weather'][0]['description'] # 
            }

    return current_temp, current_weather, forecast # <-- return current weather conditions and 5-day forecast

# Get weather for a location
location = input("Enter a location: ") # <-- get location from user
current_temp, current_weather, forecast = get_weather(location) # <-- call get_weather function

# Print current weather conditions
print(f'Current temperature in {location}: {current_temp}') # <-- print current temperature
print(f'Current weather in {location}: {current_weather}') # <-- print current weather

# Print forecast for next 5 days
print("\n5-day forecast:") # <-- print header
for date, weather in forecast.items(): # <-- loop through forecast dictionary
    print(f'{date}: Temperature: {weather["temp"]}, Weather: {weather["weather"]}') # <-- print date, temperature, and weather
```