# from pyvirtualdisplay import Display
from selenium import webdriver
import pandas as pd

use_list = []


# display = Display(visible=0, size=(800, 600))
# display.start()

driver = webdriver.Chrome("D:\\softwares\\chromedriver_win32\\chromedriver.exe")

def process(row):
    # matches =  str(row['URL'])
    driver.set_page_load_timeout(30)
    driver.get(str(row['URL']))
    driver.maximize_window()
    driver.implicitly_wait(20)
# driver.get_screenshot_as_file("./screenshot/fb.png")
#print(driver.title)
#assert "Gmail" in driver.title
driver.find_element_by_class_name("eyBreadcrumbs")
driver.quit()

if __name__=='__main__':
    df = pd.read_csv("E:\\projects\\AF\\category breadcrumbs\\scraping.csv").fillna('')
    df['breadcrumbs'] = ''
    df.apply(process, 1)
    # df['breadcrumbs'] =
    df.to_csv("E:\\projects\\AF\\category breadcrumbs\\scraped.csv", index=False)

# display.stop()