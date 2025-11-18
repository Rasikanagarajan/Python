class service:
    def __init__(self,data):
        self.data=data
        self.next=None
class ser1:                        
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=service(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def delete(self):
        if not self.head:
            print("empty")
        if not self.head.next:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        print(None)

name=input("ENter the name : ")
vehicle=input("Enter the vehicle name : ")

d=ser1()
d.insert(name)
d.insert(vehicle)
d.delete()
d.traverse()
