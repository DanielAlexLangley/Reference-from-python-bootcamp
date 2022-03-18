
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import datetime

endTime = datetime.datetime.now() + datetime.timedelta(minutes=5)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(10)
driver.maximize_window()
while True:
    if datetime.datetime.now() >= endTime:
        break

    # CLick the cookie:
    big_cookie = driver.find_element(by=By.ID, value="bigCookie")
    for _ in range(0, 5):
        big_cookie.click()

    # Variable of how many cookies I have:
    cookies = driver.find_element(by=By.ID, value="cookies").text

    # Buy something:
    for _ in range(0, 18):
        item_store = driver.find_element(by=By.ID, value=f"product{0}")
        if item_store.get_attribute("class") == "product unlocked enabled":
            item_store.click()

driver.quit()
