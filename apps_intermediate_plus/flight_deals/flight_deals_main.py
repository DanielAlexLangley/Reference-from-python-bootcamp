
# https://gist.github.com/angelabauer/99301f807578ad8b6f54e8fb8ec7162b
# https://gist.github.com/TheMuellenator/4d730d38818d935a9ce4ad9d7a817138
# Those github's are the professor's version.

from flight_deals_flight_search import FlightSearch
from flight_deals_data_manager import DataManager

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
sheety_json_all = data_manager.get_sheety_all()

if sheety_json_all[0]["iataCode"] == "":
    for row in sheety_json_all:
        flight_search = FlightSearch()
        code = flight_search.get_code(row)
        row["iataCode"] = code

data_manager.data_all = sheety_json_all
data_manager.update_codes()

flight_search = FlightSearch()
flight_search.get_flight_data(data_completed=data_manager.data_all)
