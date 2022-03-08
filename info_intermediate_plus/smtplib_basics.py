
# SMTP
# Simple Mail Transfer Protocol
# SMTP contains all the rules about how email is sent around the internet.

# SMTPlib
# Allows us to send email to any address on internet.

# https://mailtrap.io/
# This site provides free smtp credentials for testing.

import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: TEST 3
To: {receiver}
From: {sender}

This is a TEST 3 e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("x", "x")  # Have to enter info from mailtrap.io
    server.sendmail(sender, receiver, message)

# import smtplib
# my_email = "real_email@gmail.com"
# my_password = "real_password"
# connection = smtplib.SMTP("smtp.gmail.com")  # Creates object from class SMTP.
# connection.starttls()  # TLS means transport layer security. This encrypts our connection to our email server.
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addy=my_email,
#     to_addrs="fake@gmail.com",
#     msg="Subject:Hello\n\nThis is the body of the email."
# )
# connection.close()
