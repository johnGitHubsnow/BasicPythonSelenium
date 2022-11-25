import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

input_boxes = list(driver.find_elements(By.CLASS_NAME, "text_field"))

print(len(input_boxes))

input_boxes[0].send_keys("Vamsi")
input_boxes[1].send_keys("Reddy")
input_boxes[2].send_keys("987654321")
input_boxes[3].send_keys("india")
input_boxes[4].send_keys("bangalore")
input_boxes[5].send_keys("sd@gmail.com")
time.sleep(5)
driver.close()
