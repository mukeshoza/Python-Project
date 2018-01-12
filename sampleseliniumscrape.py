from selenium import webdriver
import pandas as pd

test = list()

driver = webdriver.Chrome("D:\\softwares\\chromedriver_win32\\chromedriver.exe")

for url in [""]:
    driver.get(url)

    df = driver.find_element_by_class_name("eyBreadcrumbs").text
    test.append(df)
    print(df)
    # driver.find_element_by_link_text("Clear cache").click()
driver.close()
pd.DataFrame(data=test, columns=['title']).to_csv("sample.csv")
