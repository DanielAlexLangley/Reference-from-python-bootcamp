
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME_RAW = os.environ.get("ENV_VAR_TWITTER_USERNAME")
TWITTER_USERNAME = f"@{TWITTER_USERNAME_RAW}"
TWITTER_PASSWORD = os.environ.get("ENV_VAR_TWITTER_password")


class InternetSpeedTwitterBot:

    def __init__(self):

        # SELF VARIABLES
        self.speed_down = 0
        self.speed_up = 0

        # OPENS FIREFOX TO SPEEDTEST
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("https://www.speedtest.net/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(5)

    def get_internet_speed(self):

        # RUNS SPEED TEST
        button_start = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test.test-mode-multi")
        button_start.click()
        time.sleep(90)

        # CLICK AWAY POP UP IF IT POPS UP
        try:
            button_pop_up_dismiss = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a")
            button_pop_up_dismiss.click()
        except NoSuchElementException:
            print("No pop up.")

        # SAVES RESULTS
        self.speed_down = self.driver.find_element(by=By.CLASS_NAME, value="result-data-large.number.result-data-value.download-speed").text
        self.speed_up = self.driver.find_element(by=By.CLASS_NAME, value="result-data-large.number.result-data-value.upload-speed").text

    def tweet_at_provider(self):

        # OPENS A NEW TAB TO TWITTER
        self.driver.execute_script("window.open('about:blank', 'secondtab');")
        self.driver.switch_to.window("secondtab")
        self.driver.get('https://twitter.com/')
        time.sleep(4)

        button_sign_in = self.driver.find_element(by=By.CLASS_NAME, value="css-901oao.r-1awozwy.r-1cvl2hr.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0")
        button_sign_in.click()
        time.sleep(3)

        entry_username = self.driver.find_element(by=By.CLASS_NAME, value="r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        entry_username.send_keys(TWITTER_USERNAME)
        time.sleep(1)

        button_next = self.driver.find_element(by=By.CLASS_NAME, value="css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu")
        button_next.click()
        time.sleep(2)

        entry_password = self.driver.find_element(by=By.CLASS_NAME, value="r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        entry_password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)

        button_login = self.driver.find_element(by=By.CLASS_NAME, value="css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0")
        button_login.click()
        time.sleep(2)

        button_tweet = self.driver.find_element(by=By.CLASS_NAME, value="css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0")
        button_tweet.click()
        time.sleep(4)

        entry_tweet = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div")
        entry_tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.speed_down}, {self.speed_up} when I should have {PROMISED_DOWN}, {PROMISED_UP}?")
        time.sleep(3)

        button_tweet_submit = self.driver.find_element(by=By.CLASS_NAME, value="css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0")
        button_tweet_submit.click()


internet_speed_twitter_bot = InternetSpeedTwitterBot()

internet_speed_twitter_bot.get_internet_speed()

if float(internet_speed_twitter_bot.speed_down) < PROMISED_DOWN or float(internet_speed_twitter_bot.speed_up) < PROMISED_UP:
    internet_speed_twitter_bot.tweet_at_provider()
else:
    print("Good speeds today.")
