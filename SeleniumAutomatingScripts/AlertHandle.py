import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class HandleAlert():
    def AlertHandle(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
         #   executable_path=r'C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe')
        driver.maximize_window()

        driver.get('https://testautomationpractice.blogspot.com/')

        driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.close()






halert = HandleAlert()
halert.AlertHandle()