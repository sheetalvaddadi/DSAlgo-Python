class BST:
    def __init__(self, val =None):
        self.val = val
        self.right = None
        self.left = None

    def add_node(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val ==val:
            return
        if val<self.val:
            if self.left is not None:
                return self.left.add_node(val)
            self.left =BST(val)
            return
        if self.right is not None:
            return self.right.add_node(val)
        self.right =BST(val)
        return

    '''def invert(self, root):
        if root is None:
            return None
        self.right, self.left = self.left, self.right
        return self.right.invert(root)'''

    def inorder(self, vals =[]):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

if __name__ =="__main__":
    b = BST()
    b.add_node(3)
    b.add_node(45)
    b.add_node(5)
    b.add_node(6)
    print(b.inorder())