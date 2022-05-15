# m3lab.py
# daniel bigler
# oct 7, 19 csc221

# main program for the room lab
# this should make a few rooms, then iterate through them

from room import Room

# quick test
start = Room("The Void","You should never see this room")
kitchen = Room("Kitchen", "The kitchen")
livingRoom = Room("Living room","The living room")
bedroom = Room("Bedroom", "The bedroom")
closet = Room("Closet", "The closet")
attic = Room("Attic", "The attic")
basement = Room("Basement", "The basement")

rooms = []
rooms.append(start)
rooms.append(kitchen)
rooms.append(livingRoom)
rooms.append(bedroom)
rooms.append(closet)
rooms.append(attic)
rooms.append(basement)

for room in rooms:
    #print("You are in", room[0])
    #print("Description:", room[1])
    print("Moving to a new room...")
    print(room)
