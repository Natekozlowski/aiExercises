# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
import venv
# loading variables from .env file
load_dotenv()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#time imports
import time
from datetime import datetime as dt

service = Service(os.getenv("PATH_TO_CHROMEDRIVER"))

def get_driver():
# Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    #Create the Driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def write_file(text):
    #method to write scraped data to text file
    filename = f"{dt.now().strftime('%Y-%m-%d.%H.%M.%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def clean_text(text):
    #Extract a string from a larger string
    output = text.split("Welcome ")[1]
    return output

def main():
    driver = get_driver()
    #create a wait that allows time for the dynamic text to appear
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_username"))
        ).send_keys(os.getenv("USER_LOGIN"))
    element = driver.find_element(By.ID, "id_password").send_keys(os.getenv("USER_PW") + Keys.RETURN)
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/h1[1]")))
    text = clean_text(element.text)
    write_file(text)
main()