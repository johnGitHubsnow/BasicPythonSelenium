import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#Radio Buttons implimentation
status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()
print(status)
driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()
status_s = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()
print(status_s)
#checkbox
driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()
driver.find_element(By.XPATH, "//label[normalize-space()='Saturday']").click()
time.sleep(8)


driver.close()