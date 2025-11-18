class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
 
class avl:
    def get_height(self, root):
        if not root:
            return 0
        return root.height
 
    def balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
 
    def right_rotate(self, z):
        y = z.left
        t3 = y.right
 
        y.right = z
        z.left = t3
 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
        return y
 
    def left_rotate(self, z):
        y = z.right
        t3 = y.left
 
        y.left = z
        z.right = t3
 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
        return y
 
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.balance(root)
 
        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root
 
    def min_value(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current
 
    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # node with two children: get inorder successor
            temp = self.min_value(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
 
        if root is None:
            return root
 
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.balance(root)
 
        # Balancing cases
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root
 
    def preorder(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
 
# Example run
if __name__ == "__main__":
    a = avl()
    root = None
    e = [78, 34, 23, 85, 8]
    for i in e:
        root = a.insert(root, i)
    a.preorder(root)    # prints preorder
    print()
    root = a.delete(root, 85)
    a.preorder(root)
    print()
 
 