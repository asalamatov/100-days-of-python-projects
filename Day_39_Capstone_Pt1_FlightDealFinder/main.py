#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager



data_manager = DataManager()
sheet_data = data_manager.get_destionation_data()

if sheet_data[0]["iataCode"]=="":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_API(row["city"])
    print(f"sheet_data: \n {sheet_data}")


data = DataManager()
data_manager.destination_data = sheet_data
data.update_destination_codes()