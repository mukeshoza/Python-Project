from selenium import webdriver
import pandas as pd

test = []


# driver = webdriver.PhantomJS("E:\\projects\\comparator\comparator\\phantomjs.exe")

def process(row):
    #driver = webdriver.PhantomJS("E:\\projects\\others\\comparator\\comparator\\phantomjs.exe")
    driver = webdriver.Chrome("D:\\softwares\\chromedriver_win32\\chromedriver.exe")
    matches = str(row['url'])
    # print(matches)
    driver.get(matches)
    df = driver.find_element_by_class_name("breadcrumbs").text
    test.append(df)
    print(df)
    driver.close()


# print(df)
# driver.find_element_by_link_text("Clear cache").click()


if __name__ == '__main__':


    b = pd.read_csv("E:\\projects\\QA\Migration\\Uro Turing\\select_your_car\\scraping.csv")
    b.apply(process, 1)
    pd.DataFrame(data=test, columns=['title']).to_csv("E:\\projects\\QA\Migration\\Uro Turing\\select_your_car\\scraped_data.csv")
