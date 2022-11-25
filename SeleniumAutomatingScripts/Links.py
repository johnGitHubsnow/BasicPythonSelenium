import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.get("https://demo.guru99.com/V4/")

driver.find_element(By.NAME,"uid").send_keys("mngr434736")
driver.find_element(By.NAME, "password").send_keys("UnenyrA")
driver.find_element(By.NAME, "btnLogin").click()

links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,"Edit Customer").click()
time.sleep(5)

driver.close()
