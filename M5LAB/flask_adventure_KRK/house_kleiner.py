#house
# house_kleiner
# Kenneth Kleiner
# 21 October

# room.py - the Room class

""" Definition of the House class """
from room_kleiner import Room
from roomnode_krk import RoomNode
class House:
    def __init__(self):
        ''' defines a house(list of rooms) and the connections between them '''
        # create empty list of rooms
        self.rooms = []

        # create rooms with name and description
        room1 = Room('Laundry Room', 'Room with nothing in it. Door to Kitchen')
        room2 = Room('Kitchen', 'Room with dog in it. Exits to Laundry Room, Living Room, and Dining Room')
        room3 = Room('Living Room', 'Room with TV in it.  Exit to Kitchen and Den')
        room4 = Room('Bathroom under renovation', 'Room with bucket of water in it.  Exit to Dining Room')
        room5 = Room('Dining Room', 'Room with food in it. Exit to Den, Kitchen, and Bathroom')
        room6 = Room('Den', 'Room with chair in it.  Exit to Living Room and Dining Room')

        # populate list with rooms created above
        self.rooms = [room1, room2, room3, room4, room5, room6]

        # create node for each room
        self.room1node = RoomNode(room1)
        self.room2node = RoomNode(room2)
        self.room3node = RoomNode(room3)
        self.room4node = RoomNode(room4)
        self.room5node = RoomNode(room5)
        self.room6node = RoomNode(room6)

        # create connections/doorways between rooms
        # one in each direction        
        self.room1node.east = self.room2node
        self.room2node.west = self.room1node

        self.room2node.east = self.room3node
        self.room3node.west = self.room2node
        self.room2node.south = self.room5node
        self.room5node.north = self.room2node

        self.room3node.south = self.room6node
        self.room6node.north = self.room3node

        self.room6node.west = self.room5node
        self.room5node.east = self.room6node

        self.room5node.west = self.room4node
        self.room4node.east = self.room5node

        # set starting point
        self.startnode = self.room1node

