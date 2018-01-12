import pandas as pd
import numpy as np
import re


df = pd.read_csv('"E:\pandas\new phase 2\1-3\simple_rows_single_final__magmi_SimpleVisible.csv"', encoding = "ISO-8859-1" )
#
# #[['column_name', column_name']]
# #sk = df[['sku']]
# #rint(sk)
# #inval = re.findall('\d+', 'sk')
#
# #print(inval)
#

data = df['description']
a = data.str.findall(r'(\d[\']|\d{2}[\']|\d[\"]|\d{2}[\"])')
# (r'(\d{2}[\']|\d{2}[\"]|\d{2}[\']|\d[\']|\d[\'][\/]\d[\']|\d[\"]/\d[\'])')
#(r'(\d\d[\'], \d[\'], \d[\'], \d[\'], \d[\']|\d{2}.\d+[\"]|\d+[\"])|(\d+[\']|(\d\d \d/\d+[\"])|\d+[\']|(\d \d/\d+[\"])|\d+([\']))')
df['description'] = a

#df['b'] = np.where(df['price'] == '0','yes', 'no')
#a.to_csv('sizesnew.csv', sep = ',')
#
#print(df.columns.tolist())
print(a)
