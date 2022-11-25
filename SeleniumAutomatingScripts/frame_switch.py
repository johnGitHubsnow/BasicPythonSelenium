import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService

class Frame():
    def frame_switch(self):
        driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
        #driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")


        time.sleep(4)
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')[1]
        driver.switch_to.frame(iframe)
        driver.switch_to.frame("packageListFrame")
        driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
        print(driver.title)

        # driver.switch_to.default_content()
        # print(driver.title)
        # time.sleep(3)
        #
        # driver.switch_to.frame("packageFrame")
        # driver.find_element(By.XPATH,"//span[normalize-space()='Alert']").click()
        # print(driver.title)
        #
        # driver.switch_to.default_content()
        # time.sleep(3)
        # print(driver.title)
        #
        # driver.switch_to.frame("classFrame")
        # driver.find_element(By.XPATH, "//div[@class='topNav']//a[normalize-space()='Deprecated']").click()
        # time.sleep(3)
        # print(driver.title)
        # driver.close()

frSwitch = Frame()
frSwitch.frame_switch()

