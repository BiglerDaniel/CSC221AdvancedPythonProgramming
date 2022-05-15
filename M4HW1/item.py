""" Definition of the Room class """
class Item:
    def __init__(self, string):
        """ create a Room object """
        self.string = string
        

    def __str__(self):
        """ human readable version of Room """
        readable = self.string
        readable += "\n" # new line
        
        return readable
    
