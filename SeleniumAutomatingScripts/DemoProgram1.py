import time
from tkinter import Image

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https:amazon.in/")
driver.maximize_window()
time.sleep(5)
print(driver.current_url)
#driver.get_screenshot_as_file("amazon")
#source = driver.find_element(By.XPATH, "//div[@id = 'draggable']")
#target = driver.find_element(By.XPATH, "//div[@id = 'droppable']")

#action = ActionChains(driver)

#action.drag_and_drop(source, target)
#ele = driver.find_element(By.XPATH, "//span[@id= 'nav-link-accountList-nav-line-1']")
#ele = driver.find_element(By.XPATH, "//span[@class = 'icp-nav-language']")
#action.move_to_element(ele)
#time.sleep(3)
'''
driver.back()
time.sleep(3)
ele = driver.find_element(By.XPATH, "//a[normalize-space() = 'Customer Service']")
time.sleep(5)
driver.refresh()
'''

elements = driver.find_elements(By.XPATH, "//div[@id= 'nav-xshop-container']//a")
for i in elements:
   print(i.text)

actions = ActionChains(driver)
for _ in range(26):
    actions = actions.send_keys(Keys.TAB)
actions.perform()

driver.find_element(By.XPATH, "//a[normalize-space()='Computers']").click()

time.sleep(5)

driver.close()


