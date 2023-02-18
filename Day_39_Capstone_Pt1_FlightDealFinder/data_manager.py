import requests

sheety_endpoint = "https://api.sheety.co/8770d1eda53a01f2846505862b8a3d48/flightDeals/prices"

headers = {
    "Authorization": "Bearer qwertyuiopasdfghjklzxcvbnm",
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self) -> None:
        self.destination_data = {}
        
    def get_destionation_data(self):
        data = requests.get(url=f"{sheety_endpoint}", headers=headers).json()
        self.destination_data = data["prices"]
        print("DESTINATION DATA: ", self.destination_data)
        return self.destination_data
    
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
            print(response)
            print("DESTINATION DATA: ", self.destination_data)
            