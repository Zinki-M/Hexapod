from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Control
import ADC
import Servo
import Ultrasonic
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

#head is slightly offset
HEADOFFSETANGLE = 15

STEPDEGREES = 28.5
STEPDISTANCE = 10
NORTH = [0,35]
SOUTH = [0,-35]
EAST = [35,0]
WEST = [0,35]

currentAngle = 0

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
    currentAngle += degrees

def turnTo(absDegrees):
    """turn to absolute degrees from current position"""
    diff = absDegrees - currentAngle
    turn(diff)

def batteryPrint():
    adc = ADC.ADC()
    while RUNNING:
        print("Battery:", adc.batteryPower())
        time.sleep(10)


def walk(distance, direction=NORTH):
    """walk a distance in cm"""
    control = Control.Control()
    #one command is approximately 10 cm
    commandsToRun = distance//STEPDISTANCE
    remainder = (distance%STEPDISTANCE)
    # # turnStrength max is 35
    # turnStrength = math.floor(35 * (stepNum/commandsToRun))
    data = ['CMD_MOVE', "1", str(direction[0]), str(direction[1]), "10", "0"]
    print("Running",commandsToRun,"move commands in",direction)
    for i in range(commandsToRun):
        control.run(data)
    #walk remainder
    if remainder > 0:
        multiplier = STEPDISTANCE/remainder
        data = ['CMD_MOVE', "1", str(math.floor(direction[0]*multiplier)), str(math.floor(direction[1]*multiplier)), "10", "0"]

def sweep(low = 0, high = 180):
    """sweep head"""
    servo = Servo.Servo()
    us = Ultrasonic.Ultrasonic()

    servo.setServoAngle(0,90)
    distanceSweep = []
    for angle in range(high, low, -1):
        servo.setServoAngle(1,angle)
        distance = us.getDistance()
        distanceSweep.append(distance)
        time.sleep(0.01)
    servo.setServoAngle(1,90)
    return distanceSweep

def fullSweep():
    distances = []
    for i in range(4):
        distances.extend(sweep(45,135))
        turn(90)
    return distances

def findMaxRangeAngle(full):
    if full:
        distances = fullSweep()
    else:
        distances = sweep()

    print(distances)
    maxDistance = max(distances)

    angle = distances.index(maxDistance) + HEADOFFSETANGLE
    
    #since we sweep to both sides, subtract offset based on sweep range    
    if full:
        angle -= 45
    else: 
        angle -= 90
    return angle, maxDistance

def buzz(time):
    buzzer = Buzzer.Buzzer()
    buzzer.run("1")
    time.sleep(time)
    buzzer.run("0")

def walkToFarthestThing():
    walkDist = 50
    firstSweep = True
    while True:
        angle, dist = findMaxRangeAngle(firstSweep)
        print("Max Range is at",angle,"with",dist,"cm space")
        firstSweep = False
        if(angle > 180):
            angle -= 360
        turn(angle)
        if(dist < walkDist):
            if dist > 20:
                walk(dist)
            else:
                buzz(2)
        else:
            walk(walkDist)
    

RUNNING = True
def run():
    x = threading.Thread(target=batteryPrint)
    x.start()
    walkToFarthestThing()

run()
RUNNING = False