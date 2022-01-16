from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Control


#example:
#data=['CMD_MOVE', '1', '0', '25', '10', '0']
#Move command:'CMD_MOVE'
#Gait Mode: "1"
#Moving direction: x='0',y='25'
#Delay:'10'
#Action Mode : '0'   Angleless turn 

def turnAround():
    control = Control.Control()
    data = ['CMD_MOVE', "1", "25", "0", "10", "1"]
    for i in range(10):
        control.run(data)


def makeMoveData():
    data=['CMD_MOVE', '1', '0', '25', '10', '0']


turnAround()