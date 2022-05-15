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

class RoomNode(object):

    def __init__(self, data, north = None, south = None, east = None, \
                 west = None, northEast = None, northWest = None, \
                 southEast = None, southWest = None):
        """ instantiates a RoomNode """
        self.data = data
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northEast = northEast
        self.northWest = northWest
        self.southEast = southEast
        self.southWest = southWest

    def __str__(self):
        return str(self.data)