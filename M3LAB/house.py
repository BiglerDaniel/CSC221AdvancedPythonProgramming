# house.py
# a House contains Rooms

from room import Room
from roomnode import RoomNode


class House:
    ''' a House contains multiple Room objects '''
    
    def __init__(self):
        ''' create the house '''
        start = Room("The Void", "You should never see this room...")
        kitchen = Room("Kitchen","...a room.")
        bedRoom = Room("bedroom","It has a bed.")
        bathRoom = Room("bathroom","Old.")
        livingRoom = Room("livingroom","Not so lively.")
        basement = Room("basement","Damp basement.")
        attic = Room("attic","It's a dusty attic.")
        
        self.rooms = [start, kitchen, bedRoom, bathRoom, livingRoom, basement, attic]
        kitchenNode = RoomNode(kitchen)
        bedRoomNode = RoomNode(bedRoom)
        bathRoomNode = RoomNode(bathRoom)
        livingRoomNode = RoomNode(livingRoom)
        basementNode = RoomNode(basement)
        atticNode = RoomNode(attic)
        
        #kitchen connection nodes
        kitchenNode.north = basementNode
        kitchenNode.south = bedRoomNode
        kitchenNode.east = bathRoomNode
        kitchenNode.southWest = livingRoomNode
        
        #bedroom connection nodes
        bedRoomNode.north = kitchenNode
        bedRoomNode.northEast = bathRoomNode
        
        #bathroom connection nodes
        bathRoomNode.west = kitchenNode
        bathRoomNode.southEast = bedRoomNode
        
        #livingroom connection nodes
        livingRoomNode.northWest = kitchenNode
        livingRoomNode.north = atticNode
        
        #basement connection nodes
        basementNode.north = kitchenNode
        
        #attic connection nodes
        atticNode.south = livingRoomNode
        
        self.startNode = kitchenNode
def main():
    """ test scaffold for House """
    house = House()
    me = house.startNode
    print(me)
    me = me.north
    print(me)
    me = me.north
    print(me)
    me = me.east
    print(me)
    me = me.southEast
    print(me)
    me = me.north
    print(me)
    me = me.southWest
    print(me)
    me = me.north
    print(me)
    me = me.south
    print(me)
    me = me.northWest
    print(me)
    
if __name__ == "__main__":
    main()
