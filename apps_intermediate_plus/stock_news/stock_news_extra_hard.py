
from twilio.rest import Client
import requests
import os

DIFFERENCE_PERCENT = 0
SYMBOL = ""


def get_list_days():

    global DIFFERENCE_PERCENT, SYMBOL
    api_key_alphavantage = os.environ.get("ENV_VAR_API_KEY_ALPHAVANTAGE")

    # GET STOCK DATA
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "interval": "5min",
        "apikey": api_key_alphavantage
    }
    response = requests.get(f"https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data_stocks = response.json()
    list_days = list(data_stocks["Time Series (Daily)"])
    yesterday = float(data_stocks["Time Series (Daily)"][list_days[0]]["4. close"])
    day_before_yesterday = float(data_stocks["Time Series (Daily)"][list_days[1]]["4. close"])

    # FIND DIFFERENCE_PERCENT
    DIFFERENCE_PERCENT = ((abs(yesterday - day_before_yesterday)) / day_before_yesterday) * 100

    # CREATE SYMBOL
    if yesterday - day_before_yesterday > 0:
        SYMBOL = "🔺"
    else:
        SYMBOL = "🔻"

    # IF DIFFERENCE MORE THAN %5, THEN RETURN TRUE SO NEWS CAN BE SENT
    if DIFFERENCE_PERCENT > 2:
        news_data()


def news_data():

    env_var_api_key_twilio = os.environ.get("ENV_VAR_API_KEY_TWILIO")
    env_var_api_key_newsapi = os.environ.get("ENV_VAR_API_KEY_NEWSAPI")
    env_var_sid_twilio = os.environ.get("ENV_VAR_SID_TWILIO")
    env_var_phone_twilio = os.environ.get("ENV_VAR_PHONE_TWILIO")
    env_var_phone_mine = os.environ.get("ENV_VAR_PHONE_MINE")

    parameters = {
        "q": "Tesla",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": env_var_api_key_newsapi,
        "searchIn": "title",
    }

    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data_news = response.json()
    data_news_slice = data_news["articles"][:3]

    for _ in data_news_slice:
        global SYMBOL, DIFFERENCE_PERCENT
        headline = _["title"]
        brief = _["description"]
        client = Client(env_var_api_key_twilio, env_var_sid_twilio)
        message = client.messages.create(body=f"\n\nTSLA: {SYMBOL}{DIFFERENCE_PERCENT}%"
                                              f"\nHeadline:\n{headline}\nBrief:\n{brief}",
                                         from_=f'+{env_var_phone_twilio}',
                                         to=f'+1{env_var_phone_mine}'
                                         )
        print(message.status)


get_list_days()
