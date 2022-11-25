import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element(By.ID, "RESULT_RadioButton-9")

drp = Select(element)

#selecting dropdown options
#drp.select_by_visible_text("Morning")
#drp.select_by_index(2)
drp.select_by_value("Radio-2")

#count of dropdown
print(len(drp.options))

#printing all dropdown elements
all_options = drp.options
for option in all_options:
    print(option.text)

driver.close()