from selenium import webdriver
from selenium.webdriver.support.ui import Select
# import pandas as pd

# display = Display(visible=0, size=(800, 600))
# display.start()

driver=webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://dev.conversionsondemand.com/codadmin2/index.php")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("./screenshot/beforeexc.png")
#print(driver.title)
#assert "Gmail" in driver.title
driver.find_element_by_id("username").send_keys("hosher@exclusiveconcepts.com")
driver.find_element_by_name("password").send_keys("cod@977")
driver.find_element_by_name("login").click()
driver.find_element_by_class_name("listStore1").click()
#driver.find_element_by_xpath("//*[@id='storeListDP1'"]/ul/li[278]/a").click()
#select = Select(driver.find_element_by_css_selector("#storeListDP1 > ul > li:nth-child(278) > a"))
#select = Select(driver.find_element_by_css_selector("#storeListDP1 > ul > li:nth-child(278) > a"))
driver.find_element_by_link_text('Magento 1.9').click()
driver.find_element_by_name("deal_of_day_msg").send_keys("20% off for all the product purchased!!!")
driver.find_element_by_name("deal_of_day_msg_fontcolor").clear()   #clears the pre-defined value in the input field.
driver.find_element_by_name("deal_of_day_msg_fontcolor").send_keys("#000000")
driver.find_element_by_name("deal_of_day_link").send_keys("build.exclusiveconcepts.com/virtualhosts/build/magento1_9_2_0/")
driver.get_screenshot_as_file("./screenshot/afterexec.png")
driver.find_element_by_xpath("/html/body/div[2]/aside[1]/section/ul/li[3]/a/span").click()
driver.get_screenshot_as_file("./screenshot/pocessexec.png")


driver.quit()

# display.stop()