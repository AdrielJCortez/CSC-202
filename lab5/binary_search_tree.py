from queue_array import Queue
# adding this just so I can commit and push again (mine didn't get graded from the first autograder wave)

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        return self.root is None

    def search_h(self, key, tree_node):
        if tree_node is None:
            return False
        elif (tree_node.left is None and tree_node.right is None) and (key != tree_node.key):
            return False
        elif key == tree_node.key:
            return True
        elif key > tree_node.key:
            return self.search_h(key, tree_node.right)
        elif key < tree_node.key:
            return self.search_h(key, tree_node.left)

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.search_h(key, self.root)

    def insert_h(self, key, data, tree_node):
        if key > tree_node.key:
            if tree_node.right is None:
                tree_node.right = TreeNode(key, data)
            else:
                return self.insert_h(key, data, tree_node.right)
        elif key < tree_node.key:
            if tree_node.left is None:
                tree_node.left = TreeNode(key, data)
            else:
                return self.insert_h(key, data, tree_node.left)
        elif key == tree_node.key:
            tree_node.data = data

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            return self.insert_h(key, data, self.root)

    def find_min_h(self, tree_node):
        if tree_node.left is None:
            return tree_node.key, tree_node.data
        return self.find_min_h(tree_node.left)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            return None
        return self.find_min_h(self.root)

    def find_max_h(self, tree_node):
        if tree_node.right is None:
            return tree_node.key, tree_node.data
        return self.find_max_h(tree_node.right)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            return None
        return self.find_max_h(self.root)

    def tree_height_h(self, tree_node):
        if tree_node.left is None and tree_node.right is None:
            return 0

        left_total = 0
        right_total = 0

        if tree_node.right is not None:
            right_total += 1 + self.tree_height_h(tree_node.right)
        if tree_node.left is not None:
            left_total += 1 + self.tree_height_h(tree_node.left)

        if left_total >= right_total:
            return left_total
        else:
            return right_total

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            return None
        return self.tree_height_h(self.root)

    def inorder_list_h(self, tree_node):
        if tree_node is None:
            return []  # Base case: return an empty list if the node is None
        inorder = []
        inorder.extend(self.inorder_list_h(tree_node.left))  # Traverse left subtree
        inorder.append(tree_node.key)  # Visit current node
        inorder.extend(self.inorder_list_h(tree_node.right))  # Traverse right subtree
        return inorder

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            return []
        return self.inorder_list_h(self.root)

    def preorder_list_h(self, tree_node):
        if tree_node is None:
            return []  # Base case: return an empty list if the node is None
        inorder = []
        inorder.append(tree_node.key)  # Visit current node
        inorder.extend(self.preorder_list_h(tree_node.left))  # Traverse left subtree
        inorder.extend(self.preorder_list_h(tree_node.right))  # Traverse right subtree
        return inorder

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            return []
        return self.preorder_list_h(self.root)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000)  # Don't change this!
        if self.root is not None:
            q.enqueue(self.root)
        level_ordered = []
        while not q.is_empty():
            current_dq = q.dequeue()
            level_ordered.append(current_dq.key)
            if current_dq.left is not None and current_dq.right is None:
                q.enqueue(current_dq.left)
            elif current_dq.right is not None and current_dq.left is None:
                q.enqueue(current_dq.right)
            elif current_dq.right is not None and current_dq.left is not None:
                q.enqueue(current_dq.left)
                q.enqueue(current_dq.right)
        return level_ordered
