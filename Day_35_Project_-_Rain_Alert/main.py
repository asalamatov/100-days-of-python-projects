import requests

api_key = "52c1f2b6cb582150fc1e39cf20acf1e9"
OWM_Endpoint = "api.openweathermap.org/data/2.5/weather"
LAT, LON = 9.646298, -95.588217

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': api_key,
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=9.646298&lon=-95.588217&appid=52c1f2b6cb582150fc1e39cf20acf1e9")
response.raise_for_status()
data = response.json()
print(data)
# print(response.status_code)