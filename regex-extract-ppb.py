import pandas as pd
#import numpy as np
import re



# [['column_name', column_name']]
# sk = df[['sku']]
# inval = re.findall('\d+', 'sk')

# print(inval)

regex = r'(Ite\w+\s\w+\w+:\s\w+|' \
        r'Ite\w+\s\w+\w+:\s\w+-\w+|' \
        r'Ite\w+\s\w+\:\s\w+-\w+-\w+\D\w+\D\w+|' \
        r'Ite\w+\s+\w+:\s+\w+-\w+-\w+|' \
        r'Ite\w+\s+\w+:\s+\w+-\w+)'

        # r'(ite\w+\s+\w+\D\s+\w+-\w+-\w+-\w+-\w+-\w+|' \
        # r'it\w+ n\w+:\s\w+-\w+|Ite\w+\s\w+\D+\w+|' \
        # r'it\w+ n\w+:\s\w+-\w+|' \
        # r'Ite\w+\s\w+\D+\w+-\w+|Ite\w+\s\w+\:\s\w+-\w+|' \
        # r'Ite\w+\s\w+\:\s\w+-\w+-\w+|' \
        # r'ite\w+\s+\w+\D\s+\w+-\w+-\w+-\w+|' \
        # r'ite\w+\s+\w+\D\s+\w+-\w+-\w+-\w+-\w+|' \
        # r'ite\w+\s+\w+\D\s+\w+-\w+-\w+-\w+-\w+\D+\d+|' \
        # r'Ite\w+\s\w+\:\s\w+-\w+-\w+\D\w+\D\w+)'
use_list = []

def process(row):
    matches = re.findall(regex, str(row['scraped_data']), re.IGNORECASE)
    # mat = re.findall(regex, str(row['short_description']), re.IGNORECASE)
    # mat1 = re.findall(regex, str(row['name']), re.IGNORECASE)
    # mat2 = re.findall(regex, str(row['attr_desc_features']), re.IGNORECASE)
    # mat3 = re.findall(regex, str(row['attr_desc_supplement']), re.IGNORECASE)
    #mat5 = re.findall(regex, str(row['attr_saint']), re.IGNORECASE)
    #mat4 = re.findall(regex, str(row['ProductName']), re.IGNORECASE)

    final_list = matches
    # final_list = mat4
    #
    # print (row[0])
    # print(final_list)
    use_found = ','.join(list(set(final_list)))
    use_list.append(use_found)


if __name__=='__main__':
    df = pd.read_csv("E:\\projects\\QA\Migration\\PishPoshBaby\\scraped\\remaini_item.csv").fillna('')
    df['itemnum'] = ''
    df.apply(process, 1)
    df['itemnum'] = use_list
    df.to_csv("E:\\projects\\QA\Migration\\PishPoshBaby\\scraped\\scrapeditemnum_remai.csv", index=False)
    # print(use_list)