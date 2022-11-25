from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()

driver.implicitly_wait(15)  # execute for every line of code that is for every element

driver.get("https://demo.guru99.com/V4/")
print(driver.title)
assert "Guru99 Bank Home Page" in driver.title
driver.find_element(By.NAME, "uid").send_keys("mngr434736")
driver.find_element(By.NAME, "password").send_keys("UnenyrA")
driver.find_element(By.NAME, "btnLogin").click()

print(driver.title)
assert "Guru99 Bank Manager HomePage" in driver.title

driver.close()



