import pandas as pd
#import numpy as np
import re

regex = r'(Standi\w+|wal\w+ M\w+|si\w+ c\w+ s\w+)'


use_list = []

def process(row):
    matches = re.findall(regex, str(row['description']), re.IGNORECASE)
    mat = re.findall(regex, str(row['short_description']), re.IGNORECASE)
    mat1 = re.findall(regex, str(row['name']), re.IGNORECASE)
    mat2 = re.findall(regex, str(row['attr_desc_features']), re.IGNORECASE)
    mat3 = re.findall(regex, str(row['attr_desc_supplement']), re.IGNORECASE)
    #mat5 = re.findall(regex, str(row['attr_saint']), re.IGNORECASE)
    #mat4 = re.findall(regex, str(row['ProductName']), re.IGNORECASE)

    final_list = matches + mat1 + mat2 + mat3 + mat

    use_found = ','.join(list(set(final_list)))
    use_list.append(use_found)


if __name__=='__main__':
    df = pd.read_csv("E:\\projects\\AF\\category breadcrumbs\\Output.csv").fillna('')
    df['filter'] = ''
    df.apply(process, 1)
    df['filter'] = use_list
    df.to_csv("E:\\projects\\AF\\category breadcrumbs\\scraped.csv", index=False)
    # print(use_list)