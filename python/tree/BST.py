class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # visit root node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # might be in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            # might be in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.right
            
            # find the minimum value of right subtree and rebalance the tree
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self
    
    def delete2(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right
            
            # find the maximum value of left subtree and rebalance the tree
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 10, 5, 7, 2, 8, 9]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(5))
    # print(numbers_tree.find_max())
    # print(numbers_tree.find_min())
    numbers_tree.delete(8)
    print(numbers_tree.in_order_traversal())
