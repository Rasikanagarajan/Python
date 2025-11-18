l=[34,56,67,78]
l1=[45,39,24]
l2=l+l1
print(l2)
l3=l1*4
print(l3)
l.append(34)
print(l)
l.extend([3,67,49])
print(l)
l.remove(34)
print(l)
l.pop() #dlt
print(l)
l.sort()  #acending
print(l)
l.reverse()
print(l)
l4=l.copy()
print(l4)
print(l.count(67))

# tuple
t=(78,34,50,29)
t1=(45,30,30,28)
t2=t+t1
print(t2)
t3=t1*5
print(t3)
# del t3
# print(t3)
print(sorted(t2))
print(t1.count(30))

# set
s={67,34,90,7,34,7}
print(s)
s.add(58)
print(s)
s.update([4,89,23])
print(s)
s.remove(90)
print(s)
s.discard(7)
print(s)
s1={89,34,58,28,10}
union=s.union(s1)
print(union)
intersention=s.intersection(s1)
print(intersention)
diffrent=s.difference(s1)
print(diffrent)
syy_diffrent=s.symmetric_difference(s1)
print(syy_diffrent)

# dict
d={"name":"sam","age":4}
print(d)
d.update({"age":34,"city":"erode"})
print(d)
print(d.items())
print(d.values())
print(d.keys())
d.popitem()
print(d)
d.pop("age")
