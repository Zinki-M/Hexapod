from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Servo
import time

def zeroPosition():
    S=Servo.Servo()     
    for i in range(32):
        if (i == 10 or i == 13 or i == 31):
            S.setServoAngle(i,0)
        elif (i == 18 or i == 21 or i == 27):
            S.setServoAngle(i,180)
        else:
            S.setServoAngle(i,90)
    time.sleep(3)


def curledPosition():
    S=Servo.Servo()     
    for i in range(32):
        if (i == 10 or i == 13 or i == 31):
            S.setServoAngle(i,315)
        elif (i == 18 or i == 21 or i == 27):
            S.setServoAngle(i,225)
        else:
            S.setServoAngle(i,90)
    time.sleep(3)


def standingPosition():
    servo=Servo.Servo()
    try:
        
        for i in range(50):
            servo.setServoAngle(15,90+i)
            servo.setServoAngle(12,90+i)
            servo.setServoAngle(9,90+i)
            servo.setServoAngle(16,90+i)
            servo.setServoAngle(19,90+i)
            servo.setServoAngle(22,90+i)
            time.sleep(0.005)
        for i in range(60):
            servo.setServoAngle(14,90+i)
            servo.setServoAngle(11,90+i)
            servo.setServoAngle(8,90+i)
            servo.setServoAngle(17,90-i)
            servo.setServoAngle(20,90-i)
            servo.setServoAngle(23,90-i)
            time.sleep(0.005)
        for i in range(120):
            servo.setServoAngle(13,i)
            servo.setServoAngle(10,i)
            servo.setServoAngle(31,i)
            servo.setServoAngle(18,180-i)
            servo.setServoAngle(21,180-i)
            servo.setServoAngle(27,180-i)
            time.sleep(0.005)
        print ("\nEnd of program")      
    except KeyboardInterrupt:
        print ("\nEnd of program")

if __name__ == '__main__':
    zeroPosition()
    standingPosition()
    zeroPosition()
    curledPosition()