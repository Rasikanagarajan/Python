import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("products-100.csv")
# df1=pd.read_csv("products-100.csv")
# df3=pd.merge(df,df1,on='Price',)
# print(df3)
print(df)


# df.plot(x='Name', y='Price', kind='bar', figsize=(12,6), title='Price by Product')
# plt.show()


df.dropna()  #if we want how='all'
print(df)
print(df.fillna({'Name':"Indhumathiii",'Price':100}))