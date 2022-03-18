
# https://github.com/mozilla/geckodriver/releases
# https://github.com/mozilla/geckodriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://www.amazon.com/gp/product/B00JL6ZKFE")
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# # print("Check", price.tag_name)
# # print(price.text)  # This doesn't work here, but might work depending on the method used.
# print(price)
# print(price.tag_name)
# print(price.get_attribute('innerHTML'))
# # driver.close()  # Closes active tab.
# driver.quit()  # Closes entire browser.
#
# # If we found a logo image:
# # print(logo.size)
#
# # See lesson 414 for example of how to use find_element to find a specific element even though
# # that specific element doesn't have any unique selectors.
#
# # If you can't find the element by css selectors, and if all else fails to find the element,
# # One that will always work is the XPath.
# # https://www.w3schools.com/xml/xpath_intro.asp
# # XPath lets you locate a specific element by path structure.
# # In the browser, find the element you want to find the path for,
# # right click it, click inspect,
# # in the developer tools, find the element in the inspector,
# # right click it and click copy > XPath.
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://github.com/")
# link_name = driver.find_element(by=By.XPATH, value="/html/body/footer/div[1]/div/div[2]/ul/li[1]/a")
# print(link_name.tag_name)
# print(link_name.text)
# driver.quit()
#
# # driver.maximize_window() might help if elements are hidden due to resizing.
#
# # Exercise:
# # https://www.python.org/
# # Make a dictionary of the 5 items on that page under "Upcoming Events".
# # The keys will be 0-4, and the values will be a dictionary with a time key and name key,
# # where the time key is date in the format it's listed in on the site: 'YYYY-MM-DD'
# # and the name key is the name of the event.
# # Then print dictionary to console.
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://www.python.org/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# dict_data = {_ - 1: {"time": driver.find_element(by=By.XPATH,
#                                                  value=f"/html/body/div/div[3]/div/section"
#                                                        f"/div[3]/div[2]/div/ul/li[{_}]/time").text,
#                      "name": driver.find_element(by=By.XPATH,
#                                                  value=f"/html/body/div/div[3]/div/section"
#                                                        f"/div[3]/div[2]/div/ul/li[{_}]/a").text}
#              for _ in range(1, 6)}
# driver.quit()
# print(dict_data)
#
# # Exercise:
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# driver.implicitly_wait(10)
# number_articles = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# number_articles.click()
# driver.quit()
# print(number_articles.text)
#
# # Exercise:
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# driver.implicitly_wait(10)
# all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
# all_portals.click()
# # driver.quit()
#
# # Exercise:
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# driver.implicitly_wait(10)
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# driver.quit()
#
# # Exercise:
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# driver.implicitly_wait(10)
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# # driver.quit()
#
# # Exercise:
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# driver.implicitly_wait(10)
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.submit()
# # driver.quit()
#
# # Exercise:
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver.get("http://secure-retreat-92358.herokuapp.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# search = driver.find_element(by=By.NAME, value="fName")
# search.send_keys("FirstName")
# search = driver.find_element(by=By.NAME, value="lName")
# search.send_keys("LastName")
# search = driver.find_element(by=By.NAME, value="email")
# search.send_keys("RealEmail")
# search = driver.find_element(by=By.CLASS_NAME, value="btn")
# search.submit()
# driver.quit()
