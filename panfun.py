import pandas as pd
import numpy as np
import re

df = pd.read_csv('sa1.csv').fillna('')

# [['column_name', column_name']]
# sk = df[['sku']]
# inval = re.findall('\d+', 'sk')

# print(inval)

regex = r'([\d]+([\D])?[\d]*([\D])?[\d]*\"(\s)*)'


def process(row):
    data = str(row['description'])
    matches = re.findall(regex, data)

    for match_num, match in enumerate(matches):
        print(match.group())
    exit()
df['description'] = df.apply(process, 1)

print(matches)