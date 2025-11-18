class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class New:
    def __init__(self):
        self.head=None
        self.current=None
    def insert(self,data):
        new_song=Node(data)
        if not self.head:
            self.head=new_song
            self.current=new_song
            return
        new_song.next=self.head
        self.head.prev=new_song
        self.head=new_song
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        print("None")

dou=New()
dou.insert("song1")
dou.insert("song2")
dou.insert("song3")
dou.insert("song4")
dou.insert("song5")
dou.print()


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class New:
    def __init__(self):
        self.head = None
        self.current = None

    def insert(self, data):
        new_song = Node(data)
        if not self.head:

            self.head = new_song
            self.current = new_song
        else:

            new_song.next = self.head
            self.head.prev = new_song
            self.head = new_song

            self.current = new_song

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print("None")

dou = New()
dou.insert("song1")
dou.insert("song2")
dou.insert("song3")
dou.insert("song4")
dou.insert("song5")
dou.print()

print("Current song:", dou.current.data)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class music:
    def __init__(self):
        self.head=None
        self.current=None

    def insert(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.current=new_node

            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print("The next song is:",self.current.data)
        else:
            print("There is no next playlist!")
    def previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print("The previous song is:",self.current.data)
        else:
            print("Tere is no previous song!")

    def print(self):
        temp=self.head
        while temp:

            print(temp.data)
            temp=temp.next
        print("None")        
mu=music()
mu.insert("molody")
mu.insert("kuthu vibezz")
mu.insert("chill vibez")
mu.print()
print("Current song:", mu.current.data)
mu.previous()
mu.next()
print("Current song:", mu.current.data)

mu.print()