class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self):
        if not self.head:
            print("empty")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        # More than one node — delete head node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def print(self):
        if not self.head:
            print("empty")
            return
        temp = self.head
        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")

        
    def insert_end(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            new.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new
            new.next=self.head
    def delete_end(self):
        if not self.head:
            print("empty")
        if self.head.next==self.head:
            self.head=None
            return
        else:
            temp=self.head
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next=self.head

# Test code
dll = CLL()
dll.insert(87)
dll.insert(67)
dll.insert(34)
dll.print()

dll.insert(26)
dll.insert(25)
dll.print()

dll.delete()
print("data delete")
dll.print()

dll.delete()
print("data delete")
dll.insert_end(34)
dll.insert_end(24)
dll.insert_end(19)
dll.insert_end(78)
dll.print()
dll.delete_end()
dll.print()
