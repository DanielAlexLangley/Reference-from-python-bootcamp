
# https://dashboard.sheety.co/

import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):

        self.env_var_api_key_sheety = os.environ.get("ENV_VAR_API_KEY_SHEETY")
        self.endpoint_sheety = f"https://api.sheety.co/{self.env_var_api_key_sheety}/flightDeals/prices"

        self.env_var_bearer_token_sheety = os.environ.get("ENV_VAR_BEARER_TOKEN_SHEETY")
        self.bearer_token = f"Bearer {self.env_var_bearer_token_sheety}"

        self.data_all = {}

    def get_sheety_all(self):

        header = {
            "Content-Type": "application/json",
            "Authorization": self.bearer_token,
        }

        endpoint_sheety = f"https://api.sheety.co/{self.env_var_api_key_sheety}/flightDeals/prices"
        response = requests.get(url=endpoint_sheety, headers=header)
        response.raise_for_status()
        result = response.json()
        result_prices = result["prices"]
        return result_prices

    def update_codes(self):

        header = {
            "Authorization": self.bearer_token,
        }

        for city in self.data_all:
            code = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{self.endpoint_sheety}/{city['id']}", headers=header, json=code)
            response.raise_for_status()
