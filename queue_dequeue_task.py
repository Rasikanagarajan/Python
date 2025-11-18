# queue-hp
# dequeue-chat premium

# class hp:
#     def __init__(self):
#         self.hp=[]
    
#     def insert (self,name,age,disease):
#         self.hp.append(name)
#         self.hp.append(age)
#         self.hp.append(disease)
#     def dequeue (self):
#         self.hp.pop(0)
        
# q=hp()
# name=input("Enter the name : ")
# age=int(input("Enter the age : "))
# disease=input("enter the disease : ")
# q.insert(name,age,disease)

    
# patient=input("Enter you are a new patient : [1.yes,2.No] : ")
# if patient == "1":
#         name=input("Enter the name : ")
#         age=int(input("Enter the age : "))
#         disease=input("enter the disease : ")
#         q.insert(name,age,disease)
# else:
#         print("No more patients")

# print(q.hp)

# *****************************************************************************



# from collections import deque

# class premium(Exception):
#     def __init__(self):
#         self.deque=deque()
#     def add_start(self,name,product,price):
#         self.name=name
#         self.product=product
#         self.price=price
#     def add_end(self,name,product,price):
#         self.name=name
#         self.product=product
#         self.price=price

# choice = input("If u have a premium ? [1.yes,2.no] : ")
# try:
#     name=input("Enter the name : ")
#     product=input("Enter the product : ")
#     price=int(input("Enter the price : "))
# except Exception as e:
#     print("Invalid",e)

from collections import deque

class chat():
    def __init__(self):
        self.deque=deque()
    def start(self,name,premium):

        if premium=="yes":
            self.deque.appendleft(name)
        else:
            self.deque.append(name)
    def customer(self):
        print(self.deque)
    def insert(self):

        try:
            while True:
                name=input("ENter the name : ")
                premium=input("if you have a premium [1.yes,2.no] : ")
                self.start(name,premium)

                choice=input("ENter another name [1.yes,2.no] : ")
                if choice == "1":
                    self.insert()
                else:
                    break;


        except Exception as e:
            print("Invalid",e)
        else:
            self.customer()
        finally:
            print("Executed")
dd=chat()
dd.insert()