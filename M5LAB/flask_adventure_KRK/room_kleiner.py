# m3lab - part 1
# Kenneth Kleiner
# 21 October

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
        readable += "\n" # new line
        
        return readable
    
