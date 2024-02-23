import os
import requests

SHEETY_PRICES_ENDPOINT = f"{os.environ.get('sheety_prices_enpoint')}/myFlightDeals/prices"
SHEETY_USERS_ENPOINT = f"{os.environ.get('sheety_prices_enpoint')}/myFlightDeals/users"
HEADER = {
    "Authorization": os.environ.get("sheety_authentication"),
    "Content-Type": "application/json",
}
class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = []
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=HEADER,
                json=new_data
            )
            print(response.text)

    def get_customer_data(self):
        customers_endpoint = f"{SHEETY_USERS_ENPOINT}"
        response = requests.get(customers_endpoint, headers=HEADER)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data