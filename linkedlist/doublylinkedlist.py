class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dls:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def delete(self):
        if not self.head:
            print("empty")
            return
        if not self.head.next:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dou=dls()
dou.insert(65)
dou.insert(55)
dou.insert(90)
dou.delete()
dou.print()


class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dle:
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
        new_node.prev=temp
    def delete(self):
        if not self.head:
            print("empty")
        if not self.head.next:
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
do=dle()
do.insert("hello")
do.insert("Rasika")
do.insert("how")
do.insert("are you?")
do.insert("darling!!")
do.print()
do.delete()
do.print()