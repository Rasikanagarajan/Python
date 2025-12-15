import re
text="hello i am python code and my id is 767679800 909565"
u=re.match("hello",text)
print(u)
u=re.search("\d{5}",text)
print(u)
u=re.findall("\d+",text)
print(u)
 
import math
print(math.sqrt(64))
print(math.factorial(5))
print(math.pi)
print(math.sin(3))
print(math.cos(56))
print(math.tan(8))
 
 
from datetime import datetime,timedelta
 
t=datetime.now()
print(t)
tt=datetime.today()
print(tt)
 
td=tt+timedelta(days=2)
print(td)
 
ts=datetime.strptime("2025-12-11 11:34:00","%Y-%m-%d %H:%M:%S")
print(ts)

import sys
 
print(sys.argv)
print(sys.path)
 
# n=int(input("enter a number:"))
# if n<18:
#     print('hello')
#     sys.exit()
# print("bye")
 
import os
 
print(os.getcwd)
# os.mkdir("hello")
# os.mkdir("bye")
# os.remove("bye")
print(os.listdir())
 
import numpy as np
 
print(np.random.rand(3))
print(np.random.randint(1,10))
print(np.random.randn(3,3))
 
import json, pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
 
with open("d.json") as f:
    obj = json.load(f)        # obj is a dict
df = pd.DataFrame([obj])      # single row
print(df)
 
x=[1,2,3,4]
y=[10,20,30,40]
 
plt.plot(x,y)
plt.xlabel("units")
plt.ylabel("values")
plt.title("graph")
plt.show()
 

# seaborn

# df=pd.DataFrame({"x":[10,20,30,40],"y":[100,200,300,400]})
# sns.barplot(x="x",y="y",data=df)
# plt.show()
 
 