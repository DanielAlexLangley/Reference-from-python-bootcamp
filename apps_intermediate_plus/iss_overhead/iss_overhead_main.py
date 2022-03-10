
import datetime
import requests
import smtplib
import time

# GLOBAL VARIABLES (for email)
SENDER = "Private Person <from@example.com>"
RECEIVER = "A Test User <to@example.com>"
MESSAGE = f"""\
Subject: Hi Mailtrap
To: {RECEIVER}
From: {SENDER}

Go look at the ISS."""

# GLOBAL VARIABLES (other)
LAT_DALLAS = 32.777981
LNG_DALLAS = -96.796211


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_iss = response.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    print(f"ISS is at lat {iss_latitude} and lng {iss_longitude}.\nDallas is at lat 32 and long -96.")
    if LAT_DALLAS-10 <= iss_latitude <= LAT_DALLAS+10 and LNG_DALLAS-10 <= iss_longitude <= LNG_DALLAS+10:
        print("Within range.")
        return True
    else:
        print("Not within range.")


def utc_to_local(utc_hour):
    local_utc_offset = -6
    utc_hour += local_utc_offset
    if local_utc_offset > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif local_utc_offset < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def is_night():
    parameters = {
        "lat": LAT_DALLAS,
        "lng": LNG_DALLAS,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_sun = response.json()
    time_sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    time_sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    lt_sunrise = utc_to_local(time_sunrise)
    lt_sunset = utc_to_local(time_sunset)

    if time_now <= lt_sunrise or time_now >= lt_sunset:
        print("It is dark.")
        return True
    else:
        print("It is not dark.")


while True:
    print("\nNew check starting.")
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login("x", "x")
            server.sendmail(SENDER, RECEIVER, MESSAGE)
    time.sleep(20)
