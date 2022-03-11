
import datetime
import requests
import os

env_var_api_key_nutritionix = os.environ.get("ENV_VAR_API_KEY_NUTRITIONIX")
env_var_app_id_nutritionix = os.environ.get("ENV_VAR_APP_ID_NUTRITIONIX")

endpoint_post_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint_post_sheety = ""  # Add this url from sheety if I want to run this code again.

query = input("Tell me which exercises you did: ")

endpoint_post_parameters = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

headers = {
    "x-app-id": env_var_app_id_nutritionix,
    "x-app-key": env_var_api_key_nutritionix,
    "x-remote-user-id": "0",  # Set to the string "0" since documentation says to set to 0 for development mode.
}

response = requests.post(url=endpoint_post_nutritionix, json=endpoint_post_parameters, headers=headers)
response.raise_for_status()
result = response.json()

for _ in result["exercises"]:

    headers_exercises = {
        "Content-Type": "application/json",
        "Authorization": "",  # Add my authorization code from sheety if I want to run this code again.
    }

    workout = {
        "workout": {
            "date": datetime.datetime.now().strftime("%x"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": _["name"].title(),
            "duration": _["duration_min"],
            "calories": _["nf_calories"],
        }
    }

    response = requests.post(url=endpoint_post_sheety, json=workout, headers=headers_exercises)
    response.raise_for_status()
