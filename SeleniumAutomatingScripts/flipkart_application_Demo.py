import self as self
from selenium.webdriver import ActionChains, Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']").click()
action = ActionChains(driver)
#hover_ele_fashion = driver.find_element(By.XPATH, "//div[contains(text(),'Fashion')]")
hover_ele_fashion = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    driver.find_element(By.XPATH, "//div[contains(text(),'Fashion')]")))
action.move_to_element(hover_ele_fashion).perform()
time.sleep(5)
hover_ele_watches_accessories = driver.find_element(By.XPATH, "//a[normalize-space()='Watches and Accessories']")
action.move_to_element(hover_ele_watches_accessories).perform()
time.sleep(5)
elements = driver.find_elements(By.XPATH, "//div[@class = '_3XS_gI']/a")
print("elements count with count method: ", len(elements))
count = 0
for element in elements:
    print(element.text)
    count = count+1
print("no of elements are: ", count)
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Wallets']").click()
time.sleep(30)
wait = WebDriverWait(driver, 30)
brand = driver.find_element(By.XPATH, "//div[contains(text(),'Brand')]")
brand.click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search Brand']").send_keys("fastrack")
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='_24_Dny']").click()   #//div[@title='Fastrack']
time.sleep(10)
brand.click()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@placeholder='Search Brand']").clear()    #[@value = 'fastrack']
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search Brand']").send_keys("wrogn") #[@value = 'fastrack']
#action.click(search).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='_24_Dny']").click() #//div[@title='WROGN']
time.sleep(10)
brand.click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search Brand']").clear()   #[@value = 'wrogn']
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search Brand']").send_keys("jsn") # [@value = 'wrogn']
time.sleep(5)

driver.find_element(By.XPATH, "//div[@class='_24_Dny']").click()    #//div[@title='JSN']
time.sleep(10)
products = driver.find_elements(By.XPATH, "//img[@class='_2r_T1I']")
products[2].click()

#driver.find_element(By.XPATH, "(//a[@title='Men Blue Genuine Leather Wallet - Mini']"
    #                        "[normalize-space()='Men Blue Genuine Leather Wallet - Mini'])[1]").click()
time.sleep(5)
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "WROGN Men Blue Genuine Leather Wallet Blue - Price in India | Flipkart.com":
        assert True
        break

driver.find_element(By.XPATH, "//button[normalize-space()='ADD TO CART']").click()
time.sleep(10)
count_positive = 0
for i in range(1, 4):
    driver.find_element(By.XPATH, "//button[normalize-space()='+']").click()
    time.sleep(5)
    count_positive += 1
original_count = driver.find_element(By.XPATH, "//input[@value='4']").get_attribute("value")
print(original_count)
if str(count_positive) == str(original_count):
    print("actual count: ", count_positive, "expected count: ", original_count)
    assert True

time.sleep(5)
count_negative = 4
for i in range(1,4):
    driver.find_element(By.XPATH, "//button[text()='–']").click()
    time.sleep(5)
    count_negative -= 1
original_count_negative = driver.find_element(By.XPATH, "//input[@value='1']").get_attribute("value")
print(original_count_negative)
if str(count_negative) == str(original_count_negative):
    print("actual count: ", count_negative, "expected count: ", original_count_negative)
    assert True

time.sleep(5)

driver.find_element(By.XPATH, "//span[text()='Place Order']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("adassf")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
invalid_text = driver.find_element(By.XPATH, "//span[contains(text(),'Please "
                                             "enter valid Email ID/Mobile number')]").text
print(invalid_text)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("8328338674")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Vamsi@24")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(10)


driver.close()
