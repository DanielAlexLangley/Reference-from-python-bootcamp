
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import time
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME_RAW = os.environ.get("ENV_VAR_TWITTER_USERNAME")
TWITTER_USERNAME = f"@{TWITTER_USERNAME_RAW}"
TWITTER_PASSWORD = os.environ.get("ENV_VAR_TWITTER_password")


class InternetSpeedTwitterBot:

    def __init__(self):

        down = 0
        up = 0

        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("https://www.speedtest.net/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(5)

        self.speed_down = 0
        self.speed_up = 0

    def get_internet_speed(self):

        button_start = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test.test-mode-multi")
        button_start.click()
        time.sleep(50)

        self.speed_down = self.driver.find_element(by=By.CLASS_NAME, value="result-data-large.number.result-data-value.download-speed")
        self.speed_up = self.driver.find_element(by=By.CLASS_NAME, value="result-data-large.number.result-data-value.upload-speed")

        print(self.speed_down.text)
        print(self.speed_up.text)

    def tweet_at_provider(self):

        entry_username = self.driver.find_element(by=By.CLASS_NAME, value="r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        entry_username.send_keys(TWITTER_USERNAME)
        time.sleep(1)

        button_next = self.driver.find_element(by=By.CLASS_NAME, value="css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu")
        button_next.click()
        time.sleep(2)

        entry_password = self.driver.find_element(by=By.CLASS_NAME, value="r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        entry_password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)

        button_login = self.driver.find_element(by=By.CLASS_NAME, value="ss-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-peo1c.r-1ps3wis.r-1ny4l3l.r-1guathk.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu")
        button_login.click()
        time.sleep(2)


internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
# internet_speed_twitter_bot.tweet_at_provider()  # 150Mbps download, 10Mbps upload.
