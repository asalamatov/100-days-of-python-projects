# python namaz_vaktileri.py

from tkinter import *
import requests



url="https://prayertimes.api.abdus.dev/api/diyanet"




# city_name = input("Enter the city name: \n>>")
# find_city = requests.get(f"{url}/search?q={city_name}")
# find_city.raise_for_status()

# data = find_city.json()[0]
# # print(data)

# city_id = data["id"]
# # print(city_id)

list_of_countries = requests.get(f"{url}/countries").json()
# print(list_of_countries)

country_name = input("Enter the country name: \n>>")

params = {
    countries
}


list_of_cities_states = requests.get(f"{url}/countries/{country_name}/cities").json()
print(list_of_cities_states)