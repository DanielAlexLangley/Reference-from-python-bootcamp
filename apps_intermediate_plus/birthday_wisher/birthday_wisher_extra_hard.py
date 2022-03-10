import datetime
import smtplib
import random
import pandas

today_all_info = datetime.datetime.now()
NEW_MESSAGE = ""
SENDER = "Private Person <from@example.com>"
RECEIVER = "A Test User <to@example.com>"
MESSAGE = f"""\
Subject: Hi Mailtrap
To: {RECEIVER}
From: {SENDER}

[body]."""

with open("birthday_wisher_birthdays.csv") as data_file:
    data = pandas.read_csv(data_file)
    for (index, row) in data.iterrows():
        if int(row.month) == today_all_info.month and int(row.day) == today_all_info.day:
            with open(f"birthday_wisher_letter_templates/birthday_wisher_letter_{random.randint(1, 3)}.txt",
                      "r") as file:
                contents = file.read()
                new_contents = contents.replace("[NAME]", row.names)
                NEW_MESSAGE = MESSAGE.replace("[body]", new_contents)
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login("x", "x")
                server.sendmail(SENDER, RECEIVER, NEW_MESSAGE)
