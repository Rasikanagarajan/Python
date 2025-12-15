import numpy as np
 
a=[45,78,23,90]
print(type(a))
 
arr=np.array([89,56,29,69,90])
print(arr)
print(type(arr))
 
a2=np.array([[1,2,3],[8,9,0]])
a3=np.array([[[1,2,3],[8,9,0],[1,2,3],[8,9,0]]])
print(a2)
print(a3)
 
a=np.zeros([3,3])
print(a)
a=np.ones([3,3])
print(a)
a=np.arange(0,50,5)
print(a)
a=np.linspace(0,1,5)
print(a)
 
a=np.array([90,45,78,34],dtype=float)
print(a)
print(a.dtype)
a_int=a.astype(int)
print(a_int)
print(a_int.dtype)
 
# indexing
arr=np.array([89,56,29,69,90])
print(arr[3])
print(arr[:5])
print(arr[2:5])
print(arr[-2:])
print(arr[::2])
 
# slicing
a2=np.array([[1,2,3,6],[8,9,0,7],[4,5,6,8]])
print(a2[0,:])
print(a2[:,1])
print(a2[1:3,1:3])
 
ac=arr.copy()
ac[2]=67
print(arr)
print(ac)
ac=arr.view()
ac[2]=67
print(arr)
print(ac)

arr=np.array([89,56,29,69,90,89])
print(arr)
print(arr.shape)
 
rs=arr.reshape(2,3)
print(rs)
 
print(arr.max())
print(arr.min())
 
print(np.max(rs))
print(np.min(rs))
 
for row in rs:
    for col in row:
        print(col,end=" ")
print()
 
for x in np.nditer(rs):
    print(x)
 
a=np.array([2,5,7])
b=np.array([8,4,6])
join=np.concatenate((a,b))
print(join)
 
split=np.array_split(join,2)
print(split)
arr=np.array([89,56,29,69,90,89])
num=np.where(arr>50)
print(num)
 
s=np.sort(arr)
print(s)
 
f=arr[arr>55]
print(f)