class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if (self.val is None):
            self.val = val
            return
        if (val == self.val):
            return
        if (val < self.val):
            if (self.left is not None):
                return self.left.insert(val)
            self.left = BSTNode(val)
            return
        if (self.right is not None):
            return self.right.insert(val)
        self.right = BSTNode(val)
        return

    def dfs_inorder(self, vals=[]):
        if (self.left is not None):
            self.left.dfs_inorder(vals)
        if (self.val is not None):
            vals.append(self.val)
        if (self.right is not None):
            self.right.dfs_inorder(vals)
        return vals

    def dfs_preorder(self, vals=[]):
        if (self.val is not None):
            vals.append(self.val)
        if (self.left is not None):
            self.left.dfs_preorder(vals)
        if (self.right is not None):
            self.right.dfs_preorder(vals)
        return vals

    def dfs_postorder(self, vals=[]):
        if (self.left is not None):
            self.left.dfs_postorder(vals)
        if (self.right is not None):
            self.right.dfs_postorder(vals)
        if (self.val is not None):
            vals.append(self.val)
        return vals

    def bfs(self):
        bfs_list = []
        queue = []
        queue.insert(0,self)
        while(len(queue) > 0):
            self = queue.pop()
            bfs_list.append(self.val)
            if(self.left is not None):
                queue.insert(0,self.left)
            if(self.right is not None):
                queue.insert(0,self.right)
        return bfs_list

    def exists(self, val):
        if (val == self.val):
            return True

        if (val < self.val):
            if (self.left is None):
                return False
            return self.left.exists(val)

        if (self.right is None):
            return False
        return self.right.exists(val)

    def height(self,root):
        if (root is None):
            return 0
        leftAns = self.height(root.left)
        rightAns = self.height(root.right)
        return max(leftAns, rightAns) + 1

    def invert(self, node):
        if (node is None):
            return None
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
        return node

    def find_max(self):
        if (self.right is None):
            return self.val
        return self.right.find_max()

    def find_min(self):
        if (self.left is None):
            return self.val
        return self.left.find_min()

    def delete(self, val):
        if (val < self.val):
            if (self.left is not None):
                self.left = self.left.delete(val)
        elif (val > self.val):
            if (self.right is not None):
                self.right = self.right.delete(val)
        else:
            if (self.left is None and self.right is None):
                return None
            elif (self.left is None):
                return self.right
            elif (self.right is None):
                return self.left

            min_val = self.right.find_min()
            self.val = min_val
            self.right = self.right.delete(min_val)
        return self

if __name__ == "__main__":
    nums = [17,4,1,20,9,23,18,34]
    root = BSTNode(17)
    for num in nums:
        root.insert(num)
    print (root.bfs())
    root.invert(root)
    print (root.bfs())
    root.delete(45)
    root.delete(100)
    print(root.dfs_inorder())
    print(root.dfs_preorder())
    print(root.dfs_postorder())
    print(root.find_max())
    print(root.find_min())
    print(root.exists(22))
    print(root.height(root))
    print (root.bfs())