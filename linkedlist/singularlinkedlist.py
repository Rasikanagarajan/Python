class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sls:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def delete(self):
        if not self.head:
            print("list is empty")
            return
        self.head=self.head.next
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data,end="=>")
            temp=temp.next
        print("none")

d=sls()
d.insert(12)
d.insert(17)
d.insert(23)
d.delete()
d.traverse()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sle:                        
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
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
            print(temp.data,end="=>")
            temp=temp.next
        print(None)
        
d=sle()
d.insert(90)
d.insert(50)
d.insert(60)
d.delete()
d.traverse()