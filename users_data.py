import requests
import os

PROJECT = "myFlightDeals"
SHEET = "users"
HEADER = {
    "Authorization": os.environ.get("sheety_authentication")
 }
BASE_URL = f"{os.environ.get('sheety_prices_enpoint')}"

class SheetyUsers:

    def post_new_row(self, first_name, last_name, email):
        endpoint_url = f"{BASE_URL}/{PROJECT}/{SHEET}"
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(endpoint_url, headers=HEADER, json=body)
        response.raise_for_status()
        data = response.json()
        print(data)