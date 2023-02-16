import requests
from datetime import datetime

TOKEN = "1234567888888765432"
USERNAME = "azamatick"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Quran Memorization Graph",
    "unit": "lines",
    "type": "float",
    "color": "shibafu",
}

headers={
    "X-USER-TOKEN":TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# go and check results on https://pixe.la/v1/users/azamatick/graphs/graph1.html

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

today = datetime(year=2023, month=2, day=14)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity" : "5",
}
"""
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
"""
# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "3",
}

response = requests.put(url = update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)