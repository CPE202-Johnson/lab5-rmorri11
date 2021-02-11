from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __lt__(self, other):
        if type(other) != TreeNode: raise TypeError
        else: return self.data < other.data

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.root != None: #if BST is not empty
            currentNode = self.root
            return self.search_helper(currentNode, key)
        else: return False
    
    def search_helper(self, currentNode, key):
        result = False
        if key == currentNode.key: #Node already exists
            result = True
        elif key < currentNode.key: #key is smaller than current node
            if currentNode.left != None:
                result = self.search_helper(currentNode.left, key)
        elif key > currentNode.key: #key is bigger than current node
            if currentNode.right != None:
                result = self.search_helper(currentNode.right, key)
        else:                       #key isn't in this branch
            result = False
        return result

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.root != None: #if BST is not empty
            currentNode = self.root
            self.insert_helper(currentNode, key, data)
        else: self.root = TreeNode(key, data)

    def insert_helper(self, currentNode, key, data):
        if key == currentNode.key: #Node already exists
            currentNode.data = data
        elif key < currentNode.key: #key is smaller than current node
            if currentNode.left == None:
                currentNode.left = TreeNode(key, data)
            else:
                self.insert_helper(currentNode.left, key, data)
        else:                    #key is bigger than current node
            if currentNode.right == None:
                currentNode.right = TreeNode(key, data)
            else:
                self.insert_helper(currentNode.right, key, data)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root != None:
            currentNode = self.root
            return self.find_min_helper(currentNode)
        else: return None
    
    def find_min_helper(self, currentNode):
        if currentNode.left == None:
            return currentNode.key, currentNode.data
        else: return self.find_min_helper(currentNode.left)


    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root != None:
            currentNode = self.root
            return self.find_max_helper(currentNode)
        else: return None
    
    def find_max_helper(self, currentNode):
        if currentNode.right == None:
            return currentNode.key, currentNode.data
        else: return self.find_max_helper(currentNode.right)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root != None:
            currentNode = self.root
            return self.tree_height_helper(currentNode)

    def tree_height_helper(self, currentNode):
        if currentNode.left != None:
            left_depth = self.tree_height_helper(currentNode.left) + 1
        else: left_depth = 0 
        if currentNode.right != None:
            right_depth = self.tree_height_helper(currentNode.right) + 1
        else: right_depth = 0

        if left_depth > right_depth: return left_depth
        else: return right_depth


    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.root != None:
            return self.inorder_list_helper(self.root, [])
        else: return []
        
    def inorder_list_helper(self, currentNode, keylist):
        if currentNode.left != None:
            keylist = self.inorder_list_helper(currentNode.left, keylist)
        keylist.append(currentNode.key)
        if currentNode.right != None:
            keylist = self.inorder_list_helper(currentNode.right, keylist)
        return keylist
    


    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.root != None:
            return self.preorder_list_helper(self.root, [])
        else: return []
        
    def preorder_list_helper(self, currentNode, keylist):
        keylist.append(currentNode.key)
        if currentNode.left != None:
            keylist = self.preorder_list_helper(currentNode.left, keylist)
        if currentNode.right != None:
            keylist = self.preorder_list_helper(currentNode.right, keylist)
        return keylist
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        if self.root != None:
            keylist = []
            q.enqueue(self.root)
            while not q.is_empty():
                currentNode = q.dequeue()
                keylist.append(currentNode.key)
                if currentNode.left != None:
                    q.enqueue(currentNode.left)
                if currentNode.right != None:
                    q.enqueue(currentNode.right)
            return keylist
        else:
            return []
        
     

q = BinarySearchTree()
q.insert(5, 5)
q.insert(1, 1)
q.insert(8, 8)
q.insert(4, 4)
q.insert(9, 9)
q.insert(3, 3)
q.insert(0, 0)

print(q.tree_height())
a = q.tree_height()
b = q.inorder_list()
#print(b)

x = BinarySearchTree()
x.insert(5)
x.insert(2)
x.insert(10)
x.insert(1)
x.insert(3)
x.insert(4)
x.insert(7)
x.insert(15)
x.insert(12)
x.insert(16)

c = x.inorder_list()
print("inorder: ", c)

d = x.preorder_list()
print("preorder: ", d)

e = x.level_order_list()
print("lvlOrder: ", e)