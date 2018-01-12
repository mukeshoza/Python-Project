# from selenium import webdriver
import pandas as pd
# from urllib.request import urlopen
# from datetime import datetime
import requests
from bs4 import BeautifulSoup

test = []


# driver = webdriver.PhantomJS("E:\\projects\\comparator\comparator\\phantomjs.exe")

def process(row):
    # driver = webdriver.PhantomJS("E:\\projects\\others\\comparator\\comparator\\phantomjs.exe")
    # driver = webdriver.Chrome("E:\\projects\\chromedriver_win32 (1)\\chromedriver.exe")
    matches = str(row['url'])
    # print(matches)
    # r = rq.get(matches)
    # print(r)
    response = requests.get(matches)
    if response.status_code != 404:
        print(response.status_code, matches)
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
        except:
            print ('error in {}').format(matches)
            exit(1)
        box_name = soup.find('div', {'class': 'orderboxContents'})

        try:
            abc = box_name.text.strip()
            test.append(abc)

        except Exception:
            print("Exception in {0}".format(matches))

            # df = driver.find_element_by_class_name("orderboxContents")

    else:
        print("{0} is 404".format(matches))
        # print(abc)
        # driver.close()


# print(df)
# driver.find_element_by_link_text("Clear cache").click()


if __name__ == '__main__':
    b = pd.read_csv("E:\\projects\\QA\\Migration\\PishPoshBaby\\urls.csv")
    b.apply(process, 1)
    pd.DataFrame(data=test, columns=['title']).to_csv("E:\\projects\\QA\Migration\\PishPoshBaby\\scraped\\scraped2.csv", encoding="utf-8")
