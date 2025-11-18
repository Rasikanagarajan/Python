# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class cll:
#     def __init__(self):
#         self.head=None
#     def insert(self,data):
#         new_name=Node(data)
#         if not self.head:
#             self.head=new_name
#             new_name.next=self.head
#         else:
#             temp=self.head
#             while temp.next!=self.head:
#                 temp=temp.next
#             temp.next=new_name
#             new_name.next=self.head
#             self.head=new_name
    
#     def delete(self):
#         if not self.head:
#             print("Nope")
#             return
        
#         if self.head.next==self.head:
#             self.head=None
#             return
        
#     def ask(self):
#         if 



#     def print(self):
#         if not self.head:
#             print("empty")
#             return
#         temp = self.head
#         while True:
#             print(temp.data)
#             temp = temp.next
#             if temp == self.head:
#                 break
#         print("back to head")

# name1=input("Enter the name 1 : ")
# name2=input("Enter the name 2 : ")
# name3=input("Enter the name 3 : ")
# name4=input("Enter the name 4 : ")
# name5=input("Enter the name 5 : ")
# name6=input("Enter the name 6 : ")
# ask=int(input("Enter how many times : "))
# cll1=cll()
# cll1.insert(name1)
# cll1.insert(name2)
# cll1.insert(name3)
# cll1.insert(name4)
# cll1.insert(name5)
# cll1.insert(name6)
# cll1.delete()
# cll1.print()
# cll1.delete()
# cll1.print()

                                                                                          
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class crl:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            new.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
            new.next = self.head
    def repeat(self,re):
       temp = self.head
       for i in range(re):
            print(f"Round {i+1}:")
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
            print()

    def print(self):
        if not self.head:
            print("empty")
            return
        temp = self.head
        while True:
            print(temp.data,)
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")

name1 = input("Enter the player1: ")
name2 = input("Enter the player2: ")
name3 = input("Enter the player3: ")
name4 = input("Enter the player4: ")
name5 = input("Enter the player5: ")
name6 = input("Enter the player6: ")
repeat=int(input("enter the how many time to repeat?"))
cl = crl()
cl.insert(name1)
cl.insert(name2)
cl.insert(name3)
cl.insert(name4)
cl.insert(name5)
cl.insert(name6)
cl.print()
cl.repeat(repeat)