from selenium import webdriver



def browserType(browser):
    if (browser.lower() == "chrome"):
        driver = webdriver.Chrome(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\chromedriver.exe")
    elif (browser.lower() == "edge"):
        driver = webdriver.Edge(executable_path = r"C:\Users\VREDDYK\OneDrive - Capgemini\Desktop\Drivers\msedgedriver.exe")

    driver.get("https://demo.guru99.com/V4/")

    print(driver.title)

    print(driver.current_url)

    print(driver.log_types)

    driver.close()

browserType("Chrome")