import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.selenium.dev/documentation/webdriver/interactions/alerts/")

driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

wait = WebDriverWait(driver, 20)
# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert
print(alert)
# Type your message
time.sleep(5)
alert.send_keys("Selenium")
time.sleep(10)

# Press the OK button
alert.accept()