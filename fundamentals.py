a=45
b=9.7
c="hello"
is_active=True
# list,tuple,range-sequence datatypes
# list
li=[1,2.5,"python"]
# tuple
t=(3,"java",9.4)
# dict -key pair values
d={"name":"anu","age":21}
# set-unique value
s={67,34,90,12,12}
'''
print(type(a))
print(type(b))
print(type(c))
'''
print(type(is_active))
print(type(li))
print(type(t))
print(type(d))
print(type(s))
# single line commaent
name=input("enter name")
age=int(input("enter age"))
print(type(name))
print(type(age))
print("the name is :",name)
print("age is :",age)

print("name is ",name," and my age is ",age)
print(f"name is {name} and my age is {age}")

add_number=12
ass1=23

# _num=24
# 1asd=56
# class=89

import keyword

print("keywords:",keyword.kwlist)