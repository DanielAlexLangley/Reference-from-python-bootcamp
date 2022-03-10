# API AUTHENTICATION

# API KEY
# This is what api provides use to prevent users from abusing their service. This is like your username and password.
# This lets the api provider to track how much you use the api,
# and to authorize/deny you service if you go over the limit.

# Authentication normally uses an API key, but there are other methods too.

# https://openweathermap.org/api/one-call-api

# To put this code on PythonAnywhere, I had to use this tip:
# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

from twilio.rest import Client
import requests
import os

api_key_twilio = os.environ.get("API_KEY_TWILIO")
api_key_owm = os.environ.get("OWM_API_KEY")
sid_twilio = os.environ.get("SID_TWILIO")

parameters = {
    "lat": 32.777981, # Lat and Long for Dallas
    "lon": -96.796211,
    "units": "imperial",
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key_owm
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data["hourly"][:46]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True
if will_rain:
    client = Client(api_key_twilio, sid_twilio)
    message = client.messages.create(body="It's gonna rain.", from_='+put the from number from twilio', to='+put my phone number')
    print(message.status)
