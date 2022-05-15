#
# set FLASK_APP=filename
# flask run

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/list')
def list_rooms():
    '''
    input: none
    output: the output of the original
    text adventure test (all the room),
    as a string
    '''

    

    output_str = ''
    output_str += 'test 1'
    output_str += '\ntest 2'
    return output_str

@app.route('/room_visit')
def room_visit():
    from house_kleiner import House


    ''' creates instance of house, moves through it.  Also shows what happens if you go to a non-room location '''
    myHouse = House()
    whereAmI=''

    me = myHouse.startnode
    whereAmI += "This is the startnode location"
    #print(me)

    me = me.east
    whereAmI += str(me)
    #print(me)

    me = me.south
    whereAmI += str(me)
    #print(me)

    me = me.west
    whereAmI += str(me)
    #print(me)

    me = me.east
    me = me.east
    whereAmI += str(me)
    #print(me)

    me = me.north
    whereAmI += str(me)
    #print(me)

    me = me.west
    me = me.west
    whereAmI += str(me)
    #print(me)

    me = me.north
    whereAmI += "Just to show what happens when you leave room in a direction that does not go to another room"
    #print(me)
    #print()

    me = myHouse.startnode
    whereAmI += "Back at the startnode location"
    #print(me)

    return whereAmI
