import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://demo.guru99.com/V4/")

print(driver.title)

user_ele = driver.find_element(By.NAME, "uid")

print(user_ele.is_enabled())

print(user_ele.is_displayed())

pass_ele = driver.find_element(By.NAME, "password")

print(pass_ele.is_displayed())

print(pass_ele.is_enabled())

time.sleep(3)
user_ele.send_keys("mngr434736")
time.sleep(3)
pass_ele.send_keys("UnenyrA")
time.sleep(3)
driver.find_element(By.NAME, "btnLogin").click()

print(driver.title)
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='New Customer']").click()
time.sleep(3)

radio_button_m = driver.find_element(By.XPATH, "//input[@value='m']")
radio_button_f = driver.find_element(By.XPATH, "//input[@value='f']")

print(radio_button_m.is_selected())

print(radio_button_f.is_selected())


driver.close()
