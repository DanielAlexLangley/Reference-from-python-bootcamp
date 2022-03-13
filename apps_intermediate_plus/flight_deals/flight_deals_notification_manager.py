
# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1

from twilio.rest import Client
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):

        self.env_var_api_key_twilio = os.environ.get("ENV_VAR_API_KEY_TWILIO")
        self.env_var_sid_twilio = os.environ.get("ENV_VAR_SID_TWILIO")

        self.env_var_phone_twilio = os.environ.get("ENV_VAR_PHONE_TWILIO")
        self.env_var_phone_mine = os.environ.get("ENV_VAR_PHONE_MINE")

    def send_sms(self, data_cheap_flight):

        data = data_cheap_flight

        message = f'Only $' \
                  f'{data["data"][0]["conversion"]["USD"]} to fly from ' \
                  f'{data["data"][0]["cityFrom"]}-' \
                  f'{data["data"][0]["cityCodeFrom"]} to ' \
                  f'{data["data"][0]["cityTo"]}-' \
                  f'{data["data"][0]["cityCodeTo"]} on ' \
                  f'{data["data"][0]["local_departure"]}.'

        client = Client(self.env_var_api_key_twilio, self.env_var_sid_twilio)
        message = client.messages.create(body=message,
                                         from_=f'+{self.env_var_phone_twilio}',
                                         to=f'+1{self.env_var_phone_mine}'
                                         )
        print(message.status)
