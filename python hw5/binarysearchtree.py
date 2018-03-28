class Node(object):

    left_child = None
    right_child = None
    def __init__(self, key):
        self.key = key


class BinarySearchTree(object):

    def __init__(self, root = None):
        self.root = root

    def insert(self, node):
    #  we examine the root and recursively insert the new node to the left subtree if its key is less than that of the root, 
    #  or the right subtree if its key is greater than or equal to the root.
        def insert_Node(root, node):
            if root == None:
                root = node
            else:
                if node.key >= root.key: 
                    root.right_child = insert_Node(root.right_child, node)
                else:
                    root.left_child = insert_Node(root.left_child, node)
            return root
        self.root = insert_Node(self.root, node)

    def remove(self, value):
        def remove_Node(root, value):
            if root is None:
                return
            if value < root.key:
                root.left_child = remove_Node(root.left_child, value)
            elif value > root.key :
                root.right_child = remove_Node(root.right_child, value)
            else:
                if root.left_child and root.right_child :
                    temp = root
                    temp = temp.left_child
                    while temp.right_child is not None:
                        temp = temp.right_child
                    root.key = temp.key
                    root.left_child = remove_Node(root.left_child, temp.key)
                else:
                    if root.left_child is None:
                        root=root.right_child
                    elif root.right_child is None:
                        root=root.left_child
            return root
        self.root = remove_Node(self.root, value)
        return Node(value)

    def search(self, value, node = None):
        n_current = self.root
        if node is not None:
            n_current = node # searching an empty tree
        def search_value(value, node):
            if node is None:
                return False
            if node.key == value:
                return True
            elif node.key > value:
                return search_value(value, node.left_child)
            else:
                return search_value(value, node.right_child)
        return search_value(value, n_current)


    def min(self):
        if self.root is None:
            return None # what should return if root is None?
        else:
            current_node = self.root
            while current_node.left_child is not None:
                current_node = current_node.left_child
            return current_node.key

    def max(self):
        if self.root is None:
            return None # what should return if root is None?
        else:
            current_node = self.root
            while current_node.right_child is not None:
                current_node = current_node.right_child
            return current_node.key