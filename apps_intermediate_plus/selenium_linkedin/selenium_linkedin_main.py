
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2929585269&keywords=streamer&refresh=true")
driver.implicitly_wait(10)
driver.maximize_window()

# FINDS AND CLICKS THE SIGN IN BUTTON
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# FINDS THE ENTRY FIELD FOR EMAIL AND ENTERS MY EMAIL
time.sleep(2)
entry_field_id = driver.find_element(by=By.ID, value="username")
entry_field_id.send_keys("")

# FINDS THE ENTRY FIELD FOR PASSWORD AND ENTERS MY PASSWORD
entry_field_password = driver.find_element(by=By.ID, value="password")
entry_field_password.send_keys("")

# FIND SUBMIT BUTTON AND CLICK IT
time.sleep(2)
button_submit = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button")
button_submit.click()

# SELECT EASY APPLY FILTER
time.sleep(2)
button_easy_apply = driver.find_element(by=By.ID, value="ember190")
button_easy_apply.click()

# CLICK APPLY TO FIRST JOB
time.sleep(2)
button_apply_now = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button")
button_apply_now.click()

# ENTER PHONE
time.sleep(3)
entry_field_phone = driver.find_element(by=By.XPATH, value="//*[@id=\"urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2939723789,1936848531734415514,phoneNumber~nationalNumber)\"]")
entry_field_phone.send_keys("")

# CLICK NEXT TWICE
button_next = driver.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Continue to next step"]')
button_next.click()
time.sleep(2)
button_next = driver.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Continue to next step"]')
button_next.click()

# I STOPPED HERE SINCE I COULD DO MORE AND SUBMIT THE APPLICATION,
# BUT I DON'T WANT TO SUBMIT PHONY APPLICATIONS FOR REAL JOB POSTINGS.
