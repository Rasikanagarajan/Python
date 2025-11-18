# IndentationError
if 2>9:
    print(2)
else:
    print(9)

# if if else
a,b,c=45,27,89
if a>b:
    if a>c:
        print("a is big")
    else:
        print("c s big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")

# Nested if
avg=89
if avg>=90:
    print("a grade")
elif avg>=70:
    print("b grade")
elif avg>=50:
    print("c grade")
else:
    print("no grade")

# for loop / while loop
furits=["apple","orange","graps"]
for i in ("hello"):
    print("i like ",i)

count=1
while count<=5:
    print(count)
    count+=1
# for i in range(10):
#     print(i)
# for i in range(2,10):
#     print(i)
for i in range(2,10,2):
    print(i,end=" ")

for i in furits:
    if i=="orange":
        print("match found",i)
        break
    else:
        print("match not found",i)
for i in furits:
    if i=="orange":
        print("match found",i)
        continue
    else:
        print("match not found",i)
def add():
    return 2+8
ad=add()
print(ad)
print(add())

age=int(input("enter a number"))
assert (age>=18),"less than 18 year"