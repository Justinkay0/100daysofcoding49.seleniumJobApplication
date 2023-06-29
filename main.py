from selenium import webdriver
import os
import time

URL = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'
CHROMEDRIVER = '/usr/bin/chromedriver'
USERNAME = os.environ.get('username')
PASSWORD = os.environ.get('pw')

driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

driver.get(url=URL)
driver.find_element_by_link_text("Sign in").click()
driver.find_element_by_id("username").send_keys(USERNAME)
driver.find_element_by_id("password").send_keys(PASSWORD)
driver.find_element_by_class_name("btn__primary--large").click()

time.sleep(5)
job_list = driver.find_elements_by_class_name("job-card-container")
for element in job_list:
    element.click()
    time.sleep(3)
    driver.find_element_by_css_selector(".jobs-save-button span").click()
