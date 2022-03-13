
# https://tequila.kiwi.com/portal/docs/tequila_api/locations_api

from flight_deals_notification_manager import NotificationManager
from flight_deals_dates import Dates
import requests
import os


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):

        self.env_var_api_key_tequila_wiki = os.environ.get("ENV_VAR_API_KEY_TEQUILA_KIWI")

        self.header = {
            "apikey": self.env_var_api_key_tequila_wiki
        }

    def get_code(self, row):

        parameters = {
            "term": row["city"],
        }

        response = requests.get(
            "https://tequila-api.kiwi.com/locations/query",
            headers=self.header,
            params=parameters)
        response.raise_for_status()
        data_search = response.json()
        code = data_search["locations"][0]["code"]
        return code

    def get_flight_data(self, data_completed):

        dates = Dates()
        tomorrow = dates.get_tomorrow()
        six_months = dates.get_six_months()

        for _ in data_completed:

            parameters = {
                "fly_from": "DFW",
                "fly_to": _["iataCode"],
                "date_from": tomorrow,
                "date_to": six_months,
                "price_to": _["lowestPrice"],
                "asc": 1,
                "limit": 1,
                "curr": "USD"
            }

            header = {
                "Content-Type": "application/json",
                "apikey": self.env_var_api_key_tequila_wiki,
            }

            response = requests.get("https://tequila-api.kiwi.com/v2/search", headers=header, params=parameters)
            response.raise_for_status()
            data_search = response.json()
            if data_search["_results"] > 0:
                notification_manager = NotificationManager()
                notification_manager.send_sms(data_search)

        return "done"
