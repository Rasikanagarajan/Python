class Data:
    num=1
    def show(self):
        print("this is first class")
obj=Data()
obj.show()
print(obj.num)

# variable - self,class , local
class myClass:
    num=1
    def __init__(self,name):
        self.name=name
    def grade(self):
        mark=89
        print(f" class vaiable-{myClass.num}\n self variable - {self.name}\n local variable {mark}")
s1=myClass("dev")
s2=myClass("sam")
s1.grade()
s2.grade()
# method -self,class ,static
class car:
    num=34
    def s1(self):
        print("self methoc")
    @classmethod
    def s2(cls):
        print(car.num)
    @staticmethod
    def info():
        print("inform data")
class mark:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def show(self):
        total=self.m1+self.m2+self.m3
        print(f" {self.m1} {self.m2} {self.m3} {total}")
n=int(input("enter a num:"))
d=mark(n,45,78)
d.show()
