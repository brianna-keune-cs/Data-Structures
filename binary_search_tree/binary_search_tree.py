from stack.stack import Stack
from singly_linked_list.singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        try:
            self.storage.add_to_tail(value)
        except:
            return None

    def dequeue(self):
        try:
            prev_head = self.storage.remove_head()
            return prev_head
        except:
            return None


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BSTNode(target)
        value = self.value
        if target is value:
            return True
        if target < value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        current_max = self
        while current_max.right is not None:
            current_max = current_max.right
        return current_max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if not self:
            return None
        if self.left or self.right:
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):  # left - root - right
        if not node:
            return
        node.in_order_print(node.left)
        print(node.value)
        node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):  # every level of the tree
        q = Queue()
        while node is not None:
            print(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            if len(q) > 0:
                node = q.dequeue()
            else:
                break
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):  # in order, just with an iterative solution
        s = Stack()
        while node is not None:
            if node.left:
                s.push(node.left)
            print(node.value)
            if node.right:
                s.push(node.right)
            if len(s) > 0:
                node = s.pop()
            else:
                break
        return

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):  # root - left -right
        if node == None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):  # left - right - root
        if node == None:
            return

        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)