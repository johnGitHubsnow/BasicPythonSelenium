import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.guru99.com/V4/")

driver.find_element(By.NAME, "uid").send_keys("mngr434736")
driver.find_element(By.NAME, "password").send_keys("UnenyrA")
driver.find_element(By.NAME, "btnLogin").click()
#Explicity wait execution
wait = WebDriverWait(driver,10)

ele = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='New Customer']")))

ele.click()

time.sleep(5)
driver.close()