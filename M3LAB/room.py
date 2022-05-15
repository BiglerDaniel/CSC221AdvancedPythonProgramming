# m3lab
# name
# date

# room.py - the Room class

""" Definition of the Room class """
class Room:
    def __init__(self, name, description):
        """ create a Room object """
        self.name = name
        self.description = description

    def __str__(self):
        """ human readable version of Room """
        readable = "Room name: " + self.name
        readable += "\n" # new line
        readable += "Room description: " + self.description
        
        return readable
    
