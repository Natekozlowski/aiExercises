from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#service = Service('abs path to chromedriver')

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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    #Extract a string from a larger string
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    #create a wait that allows time for the dynamic text to appear
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "text-success"))
        )
    return clean_text(element.text)
print(main())