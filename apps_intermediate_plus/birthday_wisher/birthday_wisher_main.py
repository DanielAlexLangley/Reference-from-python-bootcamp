
import datetime
import smtplib
import random

today = datetime.datetime.now()
today_weekday = today.weekday()

with open("birthday_wisher_quotes.txt") as data_file:
    list_quotes = data_file.readlines()
    quote_to_send = random.choice(list_quotes)

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Inspiration quote 13
To: {receiver}
From: {sender}

{quote_to_send}"""

if today_weekday == 1:
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("x", "x")
        server.sendmail(sender, receiver, message)
