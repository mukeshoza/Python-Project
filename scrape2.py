import requests
import pandas as pd
from bs4 import BeautifulSoup

error_list = []

url_list = []
url_content = []

def process(row):
    url = str(row['url'])
    response = requests.get(url)
    if response.status_code != 404:
        print(response.status_code, url)
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
        except:
            print('error in {}').format(url)
            error_list.append(url)
            return
        box_name = soup.find('div', {'class': ['titleMe']})

        try:
            option_content = box_name.decode_contents(formatter="html")
            if option_content:
                url_list.append(url)
                url_content.append(option_content)

        except Exception:
            print("Exception in {0}".format(url))

    else:
        print("{0} is 404".format(url))


if __name__=='__main__':
    df = pd.read_csv("E:\\projects\\QA\\Migration\\PishPoshBaby\\1.csv")
    df.apply(process, 1)

    error_df = pd.DataFrame(columns=['error_url'])
    error_df['error_url']=error_list
    error_df.to_csv('E:\\projects\\QA\Migration\\PishPoshBaby\\scraped\\error_url.csv',index=False)

    output_df = pd.DataFrame(columns=['urls','content'])
    output_df['urls'] = url_list
    output_df['content'] = url_content
    output_df.to_csv('E:\\projects\\QA\Migration\\PishPoshBaby\\scraped\\main_title_1.csv',index=False)