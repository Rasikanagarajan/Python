# list

li=["apple","orange","fruit3","banana","kiwi","pomogranate"]
li1=["grapes","dragon","avacado","sapota"]
li2=li+li1
print(li2)
print(li1*6)
li.append("fruits")
print(li)
li.extend(["fruit1","fruit2","fruit3"])
print(li)
li1.remove("sapota")
print(li1)
li1.pop()
print(li1)
li.sort()
print(li)
li.reverse()
print(li)
li7=li.copy()
print(li)
print(li.count("fruit3"))

# tuple
# t=input("ENter the names: ")
# t1=input("Enter the name2: ")
# t2=t+t1
# print(t2)
# t3=t2*4
# print(t3)
# print(sorted(t2))
# print(t1.count("Anu"))

# set

n={"rasika","anu","indhu","aruna"}
print(n)
n.add("gowri")
print(n)
n1={"shankar","rasika"}
union=n.union(n1)
print(union)
intersec=n.intersection(n1)
print(intersec)
differ=n.difference(n1)
print(differ)
symdiffer=n.symmetric_difference(n1)
print(symdiffer)

