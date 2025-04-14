# Weather App

import requests
from pprint import pprint

API_KEY = "9a641e963d4d88b86f9f6e1e5e83d3c0"

city = input("\nEnter a city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weaher_data = requests.get(base_url).json()

pprint(weaher_data)
print()