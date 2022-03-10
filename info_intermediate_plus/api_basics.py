
# API
# APPLICATION PROGRAM INTERFACES

# Definition:
# A set of commands, functions, protocols, and objects that
# programmers can use to create software or interact with an external system.

# API Endpoint:
# The location where the info can be found.
# Usually a URL.

import datetime
import requests
# The "requests" module is the most popular way for Python developers to work with APIs.
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
# Output: <Response [200]>
# This is called a response code.
# See this list of response codes:
# https://www.webfx.com/web-development/glossary/http-status-codes/
# 1XX means hold on.
# 2XX means here is your data.
# 3XX means you don't have permission to access this.
# 4XX means you screwed up the request.
# 5XX means their server screwed up somehow (like server might be down).
print(response.status_code)
response.raise_for_status()  # If we don't get a 2XX code, then this will raise an exception for us in the console.

data = response.json()
print(data)
# Can tap into this data just like a dictionary.
print(data["iss_position"])

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)

# API Parameters
# See ISS app for examples.
