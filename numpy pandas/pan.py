import pandas as pd
 
a=[45,8,34,90]
print(pd.Series(a))
 
a={
    'name':["dev","sam","anu"],
    'age':[21,23,25],
    'city':["chennai","erode","erode"]
}
df=pd.DataFrame(a)
# print(df)
# print(df.info())
# print(df.describe())
 
# df=pd.read_csv("customers-100.csv")
# # print(df)

a={
    'name':["dev","sam","anu"],
    'age':[2,23,25],
    'city':["chennai","erode","erode"]
}
df=pd.DataFrame(a)
print(df['name'])
print(df[['name','city']])
# print(df.filter(items=['name']))
 
print(df[df['age']>20])
print(df[(df['age']>=20) & (df['city']=="erode")])
 
print(df.set_index('name'))
 
 
emp={
    'name':['a','b','c','d'],
    'department':['it','it','finace','law'],
    'salary':[60000,34000,12000,45000]
}
df=pd.DataFrame(emp)
grp=df.groupby('department')['salary'].max()
print(grp)
grp=df.groupby('department')['salary'].sum()
print(grp)
 
grp=df.groupby('department').agg({'salary':['mean','max','min']})
print(grp)

df1=pd.DataFrame([{'id':[1,2,3,4],'name':["vinu","anu","dev","dlk"],'age':[23,16,28,90]}])
df2=pd.DataFrame([{'id':[1,2,3],'age':[23,16,28],'city':["erode","chennai","madurai"]}])
 
df3=pd.merge(df1,df2,on='id')
print(df3)
df4=pd.merge(df1,df2,on='id',how='outer')
print(df4)
 
df=pd.DataFrame({'month':['jan','feb','march','april'],'sale':[200,100,350,600]})
df.plot(x='month',y='sale',kind='bar',title='sale report')    #marker=0
# plt.show()
 
df1=pd.DataFrame({'id':[1,2,None,4],'name':["vinu",None,"anu","dlk"],'age':[23,16,None,90]})
print(df1)
# df2=
print(df1.dropna())
print(df1.fillna({'id':101,'age':18}))