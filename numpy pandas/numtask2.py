# max min temperature
# sales max min
# sem resahpe
# 2 branch oda employee details concatenate
# sort using lowest  highest price in ecommerse
# where use pani chovolate oda quantities
# filter 6 moths target achiever

# 1st
import numpy as nam  
temp=nam.array([20,35,67,89,56,78,98])
print(temp)
print("temperature")
print(temp.max())
print(temp.min())

# 2nd
print("max and min sales")
sales=nam.array([45000,30000,23000,56000,67000,78000])
print("sales")
print(sales.max())
print(sales.min())

# 3rd
sem=nam.array(["tam","eng","mat","python","java","aos","os","web","bigdata","linux","rdbms","oracle"])
print(sem)
rs=sem.reshape(4,3)
print(rs)

# 4th
print("employee concatenate")
emp1=nam.array(["indhu",21,"sundakkampalayam",45000])
emp2=nam.array(["mathi",21,"tnpalayam",42000])
join=nam.concatenate((emp1,emp2))
print(join)

# 5th
price=nam.array(["$21000","$50000","$45000","$34000","$68000","$72000"])
s=nam.sort(price)
print(s)

# 6th
quantity=nam.array([20,-1,56,78,23,89,59])
quan=nam.where(quantity>0)
print(quan)

# 7th
target=nam.array([300,500,600,700,3400,6700,2300,5600])
filter=target[target>550]
print(filter)