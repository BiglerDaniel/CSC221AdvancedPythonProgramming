"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class StackNode(object):

    def __init__(self, data, after = None, previous = None):
        """ instantiates a RoomNode """
        # due to being unable to use next, the code uses "after"
        self.data = data
        self.after = after
        self.previous = previous
        
    def __str__(self):
        return str(self.data)