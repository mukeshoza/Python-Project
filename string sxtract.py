import pandas as pd
import numpy as np
import re


df = pd.read_csv('finish.csv',encoding = "ISO-8859-1")

data = df['description']
a = data.str.findall(r'(\bgold plated|silver plated|silver|sterling silver|bronze|gold|24K \w+)')
#(r'(\d[\']|\d{2}[\']|\d[\"]|\d{2}[\"])')
# (r'(\d{2}[\']|\d{2}[\"]|\d{2}[\']|\d[\']|\d[\'][\/]\d[\']|\d[\"]/\d[\'])')
#(r'(\d\d[\'], \d[\'], \d[\'], \d[\'], \d[\']|\d{2}.\d+[\"]|\d+[\"])|(\d+[\']|(\d\d \d/\d+[\"])|\d+[\']|(\d \d/\d+[\"])|\d+([\']))')

df['description'] = a
#df['b'] = np.where(df['price'] == '0','yes', 'no')
# print(df.columns)
#df.to_csv('finishcsv.csv', sep = ',', index=False)
print(df)
#print(df.columns.tolist())
# print(df['description'])