
# COMMENTS FROM OTHER STUDENTS ABOUT THIS ASSIGNMENT:
#

# So, yes, I did look at the Hints, and didn't understand the JavaScript solution
# (until I looked at the comments in Angela's solution) because I have no experience of JS.
# So I found my own way to do much the same thing using pure Python:
# CODE:

# from selenium import webdriver, common
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
#
# def find_followers(self, url):
#     self.driver.get(url)
#
#     # Followers Pop-up
#     self.find_element(
#         '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
#     ).click()
#
#     # Get the first 132 followers (scroll the popup down 10 times)
#     for _ in range(10):
#         # Find the first anchor tag in the popup.
#         # This needs to be renewed each time as the list scrolls.
#         self.find_element('/html/body/div[5]/div/div/div[2]//a').send_keys(Keys.END)
#         sleep(2)  # Allow the list to update

# COMMENTS:
# I find this faster and more useful than waiting for some random time for a page to load / update:
# CODE:

# def find_element(self, xpath):
#     while True:
#         try:
#             element = self.driver.find_element_by_xpath(xpath)
#             return element
#         except common.exceptions.ElementNotInteractableException:
#             print("Element Not Interactable Exception")
#         except common.exceptions.NoSuchElementException:
#             print("No Such Element Exception")
#         finally:
#             sleep(1)

# COMMENTS:
# I hope this helps someone who is also having trouble.

# QUESTION:
# Hi, Thank you for sharing your solution. I find it really helpful. I just have a question regarding your code on
# line 13: self.find_element('/html/body/div[5]/div/div/div[2]//a').send_keys(Keys.END) I've seen the use of "//a" on
# some StackOverflow answers and they've also explained the reason for the use of it, but I forgot where I looked and
# now I'm confused on how to use it. I just want to clarify, what does the "//a" do to the xpath?
# ANSWER:
# See XPath Syntax: https://www.w3schools.com/xml/xpath_syntax.asp
# The // will attempt to find the element below the previous node.
# It does not matter how many other elements are in the tree between the two points.
# So in the above xpath '/html/body/div[5]/div/div/div[2]//a' the search will
# find the anchor tag (a) anywhere below /html/body/div[5]/div/div/div[2] in the tree.

# COMMENT:
# Since I wrote this code, I have discovered Waits. https://selenium-python.readthedocs.io/waits.html#waits
# In particular:
# driver.implicitly_wait(10) # seconds
# will wait for up to 10 seconds for an element to be found before raising an exception.
# Also useful to us would be the element_to_be_clickable condition:
# from selenium.webdriver.support import expected_conditions as EC
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
