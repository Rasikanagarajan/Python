# week days sales slicing
# 12 months salary sluce jan to july salary
# using 2 dimensional array slicing separate rows and columns , sbarrays copy and view
# backup data only in one data only copy

# 1st
import numpy as nam

week=nam.array([["s-40%","m-20%","t-30%","w-50%","th-35%","f-45%","sa-65%"],["s-40%","m-20%","t-30%","w-50%","th-35%","f-45%","sa-75%"],["s-40%","m-20%","t-30%","w-50%","th-35%","f-45%","sa-95%"]])
print(week[:,-1])

# 2nd

salary = nam.array(["jan-40k","feb-42k","mar-41k","apr-45k","may-43k","jun-47k","jul-48k","aug-49k","sep-46k","oct-50k","nov-52k","dec-55k"])
print(salary[:6])

# 3rd

marks = nam.array([[78, 85, 90, 67, 88],[80, 82, 84, 70, 86],[76, 81, 88, 65, 90]])
print(marks)
backup = marks.copy()
backup[2]=99
print(backup)

# 4th

print("\nTwo dimensional")
a=nam.ones([5,5])
print("\none row")
print(a[:1])
print("\none column")
print(a[:,0:1])
print("\n sub rows and columns")
print(a[2:,0:3])

print("copy")
print(a)
acc=a.copy()
acc[1]=4
print(acc)

print("view")
print(a)
ac=a.view()
ac[2]=5
print(a)
print(ac)
