import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.get("https://demo.automationtesting.in/Windows.html")
time.sleep(5)
print(driver.title)

driver.get("https://demo.guru99.com/V4/")

print(driver.title)
time.sleep(5)
driver.back()

print(driver.title)
time.sleep(5)
driver.forward()

print(driver.title)
time.sleep(5)
driver.close()