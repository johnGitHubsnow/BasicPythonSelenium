import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)

print(driver.current_url)

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
time.sleep(5)
print(driver.current_url)
driver.quit()
