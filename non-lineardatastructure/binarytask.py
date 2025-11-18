class parking():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class car:
    def __init__(self):
        self.root=None
    
    def insert(self,root,data):
        if not root:
            return parking(data)
        if data < root.data:
            root.left=self.insert(root.left,data)
        elif data > root.data:
            root.right=self.insert(root.right,data)

        return root
    
    def insert_data(self,data):
        self.root=self.insert(self.root,data)

    def search(self,root,key):
        if root is None or root.data==key:
            return root
        if key<root.data:
            return self.search(root.left,key)
        return self.search(root.right,key)
    
    def search_key(self,key):
        return self.search(self.root,key)
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def display(self):
        self.inorder(self.root)
        print()

ins1=int(input("ENter the car 1: "))
ins2=int(input("ENter the car 2: "))
ins3=int(input("ENter the car 3: "))
ins4=int(input("ENter the car 4: "))
ins5=int(input("ENter the car 5: "))
bt=car()
bt.insert_data(ins1)
bt.insert_data(ins2)
bt.insert_data(ins3)
bt.insert_data(ins4)
bt.insert_data(ins5)
bt.display()