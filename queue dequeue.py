class queue:
    def __init__(self):
        self.p=[]
    def insert(self,data):
        self.p.append(data)
    def dequeue(self):
        self.p.pop(0)
q=queue()
q.insert(23)
q.insert(45)
q.insert(89)
q.insert(56)
print(q.p)
q.dequeue()
print(q.p)
q.dequeue()
print(q.p)

from collections import deque

class Deque:
    def __init__(self):
        self.deque=deque()
    def insert_end(self,data):
        self.deque.append(data)
    def insert_start(self,data):
        self.deque.appendleft(data)
    def delete_end(self):
        self.deque.pop()
    def delete_start(self):
        self.deque.popleft()
dd=Deque()
dd.insert_start(56)
dd.insert_start(67)
dd.insert_start(23)
dd.insert_end(78)
dd.insert_end(12)
dd.insert_end(89)
print(dd.deque)
dd.delete_end()
print(dd.deque)
dd.delete_start()
print(dd.deque)