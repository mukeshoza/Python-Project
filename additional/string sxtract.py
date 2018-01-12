import pandas as pd
import numpy as np
import re


df = pd.read_csv('1-3\simple_rows_grouped_statues_magmi_grouped_child.csv',encoding = "ISO-8859-1")

data = df['description']
#a = data.str.findall(r'(\bgold plated|silver plated|silver|sterling silver|bronze|gold|24K \w+)')
a = data.str.findall(r'(\Fiber\w+|polymer[\s+]\w+|bronze[\s+]\w+|poly\w+|Bronze[\s]\w+)')
#(r'(\d[\']|\d{2}[\']|\d[\"]|\d{2}[\"])')
# (r'(\d{2}[\']|\d{2}[\"]|\d{2}[\']|\d[\']|\d[\'][\/]\d[\']|\d[\"]/\d[\'])')
#(r'(\d\d[\'], \d[\'], \d[\'], \d[\'], \d[\']|\d{2}.\d+[\"]|\d+[\"])|(\d+[\']|(\d\d \d/\d+[\"])|\d+[\']|(\d \d/\d+[\"])|\d+([\']))')

df['use'] = a
df.to_csv('use.csv', sep = ',')
#print(a)
