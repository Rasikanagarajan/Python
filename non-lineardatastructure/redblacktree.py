class Node:
    def __init__(self,data,color="red"):
        self.data=data
        self.color=color
        self.left=None
        self.right=None
        self.parent=None

class Redblacktree:
    def __init__(self):
        self.NIL=Node(None,color="black")
        self.root=self.NIL
    
    def left_rotate(self,x):
        y=x.right
        x.right=y.left
        if y.left!=self.NIL:
            y.left.parent=x
        y.parent=x.parent

        if x.parent is None:
            self.root=y
        elif x==x.parent.left:
            x.parent.left=y
        else:
            x.parent.right=y
            y.left=x
            x.parent=y
    def right_rotate(self,x):
        y=x.left
        x.left=y.right
        if y.right!=self.NIL:
            y.right.parent=x
        y.parent=x.parent

        if x.parent is None:
            self.root=y
        elif x==x.parent.right:
            x.parent.right=y
        else:
            x.parent.left=y
            y.right=x
            x.parent=y

    def insert(self,key):
        new_node=Node(key)
        new_node.right=self.NIL
        new_node.left=self.NIL

        parent=None
        current=self.root

        while current != self.NIL:
            parent=current
            if new_node.data < current.data:
                current=current.left
            else:
                current=current.right
            new_node.parent=parent

            if parent is None:
                self.root=new_node
            elif new_node.data<parent.data:
                parent.left=new_node
            else:
                parent.right=new_node

            if new_node.parent is None:
                new_node.color="black"
                return
            if new_node.parent.parent is None:
                return
            self.insert_fix(new_node)

def insert_fix(self,k):
        while k.parent and k.parent.color=="black":
            if k.parent ==k.parent.parent.left:
                u=k.parent.parent.right
                if u.color=="red":
                    u.color="black"
                    k.parent.color="black"
                    k.parent.parent.color="red"
                    k=k.parent.parent
                else:
                    if k==k.parent.right:
                        k=k.parent
                        self.left_rotate(k)
                    k.parent.color="black"
                    k.parent.parent.color="red"
                    self.right_rotate(k.parent.parent)
            else:
                u=k.parent.parent.left
                if u.color=="red":
                    u.color="black"
                    k.parent.color="black"
                    k.parent.parent.color="red"
                    k=k.parent.parent
                else:
                    if k==k.parent.left:
                        k=k.parent
                        self.right_rotate(k)
                    k.parent.color="black"
                    k.parent.parent.color="red"
                    self.left_rotate(k.parent.parent)
            if k==self.root:
                break
        self.root.color="black"
def delete(self,data):
            node=self.root
            while node!=self.NIL and node.data!=data:
                if data<node.data:
                    node=node.left
                else:
                    node=node.right
            if node==self.NIL:
                print("empty")
                return
            y=node
            y_original_color =y.color
            if node.left==self.NIL:
                x=node.right
                self.transparent(node,node.right)
            elif node.right==self.NIL:
                x=node.left
                self.trasparent(node,node.left)
            else:
                y=self.minimum(node.right)
                y_original_color=y.color
                x=y.right
                if y.parent==y:
                    x.parent=y
                else:
                    self.transparent(y,y.right)
                    y.right=node.right
                    y.right.parent=y
                self.transparent(node,y)
                y.left=node.left
                y.left.parent=y
                y.color=node.color
def transparent(self,u,v):
    def transparent(self,u,v):
        if u.parent is None:
            self.root=v
        elif u==u.parent.left:
            u.parent.left=v
        else:
            u.parent.right=v
        v.parent=u.parent
 
    def minimum(self,node):
        while node.left!=self.NIL:
            node=node.left
        return node
    
    