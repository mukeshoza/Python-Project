from selenium import webdriver
#from selenium.webdriver.support.ui import Select
# import pandas as pd

# display = Display(visible=0, size=(800, 600))
# display.start()

driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(60)
driver.get("https://dev.conversionsondemand.com:7443/")
driver.maximize_window()
driver.implicitly_wait(60)
# driver.get_screenshot_as_file("./screenshot/beforeexc.png")
#print(driver.title)
#assert "Gmail" in driver.title
elems = driver.find_elements_by_xpath("//*[@href]")
for elem in elems:
    print (elem.get_attribute("href"))