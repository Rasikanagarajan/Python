class Data:        
    a=1+1
    def show(self):
        print("I am Rasika")
obj=Data()
obj.show()
print(obj.a)

class D:
    a1=int(input("ENter the number"))
    a2=int(input("ENter the number"))
    o=a1+a2
    def show(self):
        print("The result is...",self.o)
obj=D()
obj.show()

# # variables

class myData:
    num=1+1
    def __init__(self,name,age,city):

        self.name=name
        self.age=age
        self.city=city
        
        print(f"{self.name} {self.age} {self.city}")

name=input("enter the name :")
age=int(input("ENter the age :"))
city=input("enter the city :")

s1 = myData(name, age, city)

# method self-cls

class method:
    num=25+24-1*8/1
    def s(self):
        print("method")
    @classmethod
    def add(cls):
        print(method.num)
obj=method()
obj.add()

