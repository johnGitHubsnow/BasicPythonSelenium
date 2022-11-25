from selenium.webdriver import ActionChains, Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("se")
time.sleep(5)
action = ActionChains(driver)
action.key_down(Keys.DOWN).send_keys(Keys.ENTER).perform()



