# from pyvirtualdisplay import Display
from selenium import webdriver
import pandas as pd

# display = Display(visible=0, size=(800, 600))
# display.start()

driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://annapurna/gbd-portal/login/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("./screenshot/fb.png")
#print(driver.title)
#assert "Gmail" in driver.title
driver.find_element_by_id("email").send_keys("yoursmukesh3@gmail.com")
driver.find_element_by_name("password").send_keys("Mukesh123")
driver.find_element_by_name("submit").click()
driver.get_screenshot_as_file("./screenshot/fb2.png")
driver.find_element_by_xpath("/html/body/div[2]/aside[1]/section/ul/li[3]/a/span").click()
driver.get_screenshot_as_file("./screenshot/fb3.png")


driver.quit()

# display.stop()