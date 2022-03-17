
# PROFESSOR'S SOLUTION:
# https://gist.github.com/angelabauer/6b2d01cf2c265910ea8c03003244939f
# https://gist.github.com/angelabauer/c354128af8f132ac3be461afa4480e74#file-main-py

from bs4 import BeautifulSoup
import requests
import smtplib
import os

# VARIABLES (ENVIRONMENTAL):
env_var_mailtrap_username = os.environ.get("ENV_VAR_MAILTRAP_USERNAME")
env_var_mailtrap_password = os.environ.get("ENV_VAR_MAILTRAP_PASSWORD")

# VARIABLES (URL AND PRICE):
url_item_to_track = "https://www.amazon.com/gp/product/B00JL6ZKFE"
target_price = 55

# GET HTML FILE OF TARGET WEBPAGE:
header = {
    "User-Agent": "My User Agent 1.0",
    "From": "personal@domain.com",
}
response = requests.get(url_item_to_track, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# FIND PRICE OF ITEM AND CONVERT TO FLOAT:
item_price = soup.select_one(selector=".a-price .a-offscreen")
# item_price_stripped = item_price.get_text().strip()
# item_price_removed = float(item_price_stripped.replace("$", ""))
item_price_removed = float(item_price.get_text().split("$")[1])

# FIND NAME OF ITEM:
name_of_item = soup.find(id="productTitle").get_text().strip()

# IF PRICE IS LOWER THAN TARGET PRICE, SEND THE EMAIL:
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"
message = f"""\
Subject: Amazon Price Drop for {name_of_item}!
To: {receiver}
From: {sender}

The product price is now ${item_price_removed}, below your target price. Buy now!."""
if item_price_removed < target_price:
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(env_var_mailtrap_username, env_var_mailtrap_password)
        server.sendmail(sender, receiver, message)
