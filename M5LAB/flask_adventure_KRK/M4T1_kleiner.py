# M4T1
# Kenneth Kleiner
# 21 October

# room.py - the Room class

""" Creates instance of house and moves through it """

from house_kleiner import House


def main():
    ''' creates instance of house, moves through it.  Also shows what happens if you go to a non-room location '''
    myHouse = House()

    me = myHouse.startnode
    print("This is the startnode location")
    print(me)

    me = me.east
    print(me)

    me = me.south
    print(me)

    me = me.west
    print(me)

    me = me.east
    me = me.east
    print(me)

    me = me.north
    print(me)

    me = me.west
    me = me.west
    print(me)

    me = me.north
    print("Just to show what happens when you leave room in a direction that does not go to another room")
    print(me)
    print()

    me = myHouse.startnode
    print("Back at the startnode location")
    print(me)


main()
