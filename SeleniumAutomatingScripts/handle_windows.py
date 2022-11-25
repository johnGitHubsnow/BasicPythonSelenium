import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class WindowHandle():
    def handle_windows(self):
        driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/Windows.html")

        driver.implicitly_wait(5)
        print(driver.current_window_handle)

        driver.find_element(By.XPATH,
                          "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
        time.sleep(5)
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.title)
            if (driver.title == "Selenium"):
                driver.find_element(By.XPATH,"//span[normalize-space()='Documentation']").click()
                print(driver.current_url)
                time.sleep(5)


windowHandle = WindowHandle()
windowHandle.handle_windows()


