class Node:
    def __init__(self, data=None, color="black"):
        self.data = data
        self.color = color  # "red" or "black"
        self.left = None
        self.right = None
        self.parent = None
 
class RedBlackTree:
    def __init__(self):
        # sentinel NIL node
        self.NIL = Node(None, color="black")
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root = self.NIL
 
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
 
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
 
    def insert(self, key):
        node = Node(key, color="red")
        node.left = node.right = node.parent = self.NIL
 
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
 
        # fixup to maintain red-black properties
        self.insert_fixup(node)
 
    def insert_fixup(self, z):
        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # uncle
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left  # uncle on other side
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"
 
    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
 
    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
 
    def delete(self, key):
        z = self.root
        while z != self.NIL and z.data != key:
            if key < z.data:
                z = z.left
            else:
                z = z.right
        if z == self.NIL:
            print("Key not found:", key)
            return
 
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self.delete_fixup(x)
 
    def delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"
 
    def traverse(self, node):
        if node != self.NIL:
            self.traverse(node.left)
            print(f'{node.data}->{node.color}', end=" ")
            self.traverse(node.right)
 
if __name__ == "__main__":
    rbt = RedBlackTree()
    e = [56, 38, 93, 78, 28]
    for i in e:
        rbt.insert(i)
 
    print("After inserts:")
    rbt.traverse(rbt.root)
    print("\n\nDelete 78:")
    rbt.delete(78)
    rbt.traverse(rbt.root)
    print()
