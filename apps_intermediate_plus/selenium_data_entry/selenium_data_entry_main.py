
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json
import time
import os

# VARIABLES
page_number = 2
url_page_one = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.6678871697162%2C%22north%22%3A37.8825399309008%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url_page_two_and_beyond = f"https://www.zillow.com/homes/for_rent/1-_beds/{page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.6678871697162%2C%22north%22%3A37.8825399309008%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# GET PAGE ONE, THEN TURN PAGE ONE INTO SOUP:
header = {
    "User-Agent": "My User Agent 1.0",
    "From": "personal@domain.com",
}
response = requests.get(url=url_page_one, headers=header)
response_text = response.text
soup = BeautifulSoup(response_text, "html.parser")

# GET ADDRESSES, URLS, AND PRICES OF EACH ITEM ON PAGE ONE:
json_contents = json.loads(soup.select_one("script[data-zrr-shared-data-key]").contents[0].strip("!<>-"))
list_addresses = []
list_urls = []
list_prices = []
for _ in json_contents["cat1"]["searchResults"]["listResults"]:
    list_addresses.append(_["address"])
    list_urls.append(_["detailUrl"])
    try:
        list_prices.append(_["price"])
    except KeyError:
        list_prices.append(_["units"][0]["price"])

for _ in list_urls:
    list_urls_index = list_urls.index(_)
    if "/b/" in _:
        list_urls[list_urls_index] = f"https://www.zillow.com" + _

# USE SELENIUM TO OPEN THE FORM:
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)

for _ in list_addresses:

    list_index = list_addresses.index(_)
    print(f"Attempt {list_index}")

    entry_address = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    entry_address.send_keys(list_addresses[list_index])

    entry_price = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    entry_price.send_keys(list_prices[list_index])

    entry_url = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    entry_url.send_keys(list_urls[list_index])

    button_submit = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    button_submit.click()
    time.sleep(1)

    button_submit_another = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    button_submit_another.click()
    time.sleep(1)

