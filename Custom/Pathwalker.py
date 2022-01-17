from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Control
import ADC
import math
import threading
import time

#example:
#data=['CMD_MOVE', '1', '0', '25', '10', '0']
#Move command:'CMD_MOVE'
#Gait Mode: "1"
#Moving direction: x='0',y='25'
#Delay:'10'
#Action Mode : '0'   Angleless turn 

STEPDEGREES = 28


def turn(degrees):
    """turn given degrees"""
    control = Control.Control()
    #one command is approximately 28.5 degrees
    stepNum = abs(degrees)/STEPDEGREES
    commandsToRun = math.ceil(stepNum)
    # turnStrength max is 35
    turnStrength = math.floor(35 * (stepNum/commandsToRun))
    data = ['CMD_MOVE', "1", str(turnStrength), "0", "10", "10"]
    print("Running",commandsToRun,"turn commands at strength",turnStrength)
    for i in range(commandsToRun):
        control.run(data)

def batteryPrint():
    adc = ADC.ADC()
    while RUNNING:
        print("Battery:", adc.batteryPower())
        time.sleep(3)


RUNNING = True
def run():
    x = threading.Thread(target=batteryPrint)
    x.start()
    turn(1080)
    RUNNING = False

