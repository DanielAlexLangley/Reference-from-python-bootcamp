
# https://github.com/mozilla/geckodriver/releases
# https://github.com/mozilla/geckodriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.amazon.com/gp/product/B00JL6ZKFE")
price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# print("Check", price.tag_name)
print(price.get_attribute('innerHTML'))

# driver.close()  # Closes active tab.
driver.quit()  # Closes entire browser.
