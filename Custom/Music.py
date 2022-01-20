from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Poses
import Servo
from Constants import *
import time

#13
noteTipOffsets = {
    "c": 90,
    "d": 90,
    "e": 90,
    "f": 80,
    "g": 70,
    "a": 50,
    "h": 45
}
#15
noteHipOffsets = {
    "c": 45,
    "d": 55,
    "e": 65,
    "f": 70,
    "g": 78,
    "a": 82,
    "h": 82
}
#14
noteKneeOffsets = {
    "c": 110,
    "d": 110,
    "e": 110,
    "f": 105,
    "g": 100,
    "a": 95,
    "h": 90
}


ducks = [("c",.5),("d",.5),("e",.5),("f",.5),("g",1),("g",1),
        ("h",.4),("h",.4),("h",.4),("h",.4),("g",1),
        ("h",.4),("h",.4),("h",.4),("h",.4),("g",1),
        ("f",.4),("f",.4),("f",.4),("f",.4),("e",1),("e",1),
        ("d",.4),("d",.4),("d",.4),("d",.4),("c",1)]

MOVETIME = 0.05

def playMusic(notes):
    Poses.pointFingers()
    servo = Servo.Servo()
    for note, duration in notes:
        servo.setServoAngle(FRONT_LEFT_HIP,noteHipOffsets[note])
        servo.setServoAngle(FRONT_LEFT_TIP,noteTipOffsets[note])
        time.sleep(MOVETIME)
        pressKey(duration-MOVETIME, noteKneeOffsets[note])
    Poses.pointFingers()


def pressKey(duration, kneePos):
    servo = Servo.Servo()
    servo.setServoAngle(FRONT_LEFT_KNEE,kneePos)
    time.sleep(duration)
    servo.setServoAngle(FRONT_LEFT_KNEE,120)

Poses.pointFingers()
playMusic(ducks)