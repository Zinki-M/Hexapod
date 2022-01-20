from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Servo
import Poses
from sys import argv


servo = Servo.Servo()
if len(argv) > 2:
    servo.setServoAngle(int(argv[1]),int(argv[2]))
else:
    Poses.pointFingers()
