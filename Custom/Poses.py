from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Servo
import time
from Constants import *

def zeroPosition():
    print("zero Position")
    S=Servo.Servo()     
    for i in range(32):
        if (i == 10 or i == 13 or i == 31):
            S.setServoAngle(i,0)
        elif (i == 18 or i == 21 or i == 27):
            S.setServoAngle(i,180)
        else:
            S.setServoAngle(i,90)
    time.sleep(1)


# def curledPosition():
#     print("curling up")
#     servo=Servo.Servo()
#     maxKnee = 0
#     maxTip = 90
#     try:
        
#         servo.setServoAngle(15,90)
#         servo.setServoAngle(12,90)
#         servo.setServoAngle(9, 90)
#         servo.setServoAngle(16,90)
#         servo.setServoAngle(19,90)
#         servo.setServoAngle(22,90)
#         time.sleep(1)

#         for i in range(maxKnee):
#             servo.setServoAngle(14,90-i)
#             servo.setServoAngle(11,90-i)
#             servo.setServoAngle(8,90-i)
#             servo.setServoAngle(17,90+i)
#             servo.setServoAngle(20,90+i)
#             servo.setServoAngle(23,90+i)
#             time.sleep(0.005)
#         for i in range(maxTip):
#             servo.setServoAngle(13,-i)
#             servo.setServoAngle(10,-i)
#             servo.setServoAngle(31,-i)
#             servo.setServoAngle(18,180+i)
#             servo.setServoAngle(21,180+i)
#             servo.setServoAngle(27,180+i)
#             time.sleep(0.005)      
#     except KeyboardInterrupt:
#         print ("\ninterrrupted")
#     time.sleep(1)

def tipToes():
    print("Standing on tiptoes")
    servo=Servo.Servo()
    maxKnee = 0
    maxTip = 90
    try:
        
        servo.setServoAngle(15,90)
        servo.setServoAngle(12,90)
        servo.setServoAngle(9, 90)
        servo.setServoAngle(16,90)
        servo.setServoAngle(19,90)
        servo.setServoAngle(22,90)
        time.sleep(1)

        for i in range(maxKnee):
            servo.setServoAngle(14,90-i)
            servo.setServoAngle(11,90-i)
            servo.setServoAngle(8,90-i)
            servo.setServoAngle(17,90+i)
            servo.setServoAngle(20,90+i)
            servo.setServoAngle(23,90+i)
            time.sleep(0.005)
        for i in range(maxTip):
            servo.setServoAngle(13,i)
            servo.setServoAngle(10,i)
            servo.setServoAngle(31,i)
            servo.setServoAngle(18,180-i)
            servo.setServoAngle(21,180-i)
            servo.setServoAngle(27,180-i)
            time.sleep(0.005)
       
    except KeyboardInterrupt:
        print ("\ninterrrupted")
    time.sleep(1)

def jumpUp():
    print("Preparing jump")
    zeroPosition()
    print("Jumping up")
    stand()
    time.sleep(1)

def stand():
    servo=Servo.Servo()

    servo.setServoAngle(14,150)
    servo.setServoAngle(11,150)
    servo.setServoAngle(8,150)
    servo.setServoAngle(17,30)
    servo.setServoAngle(20,30)
    servo.setServoAngle(23,30)
    servo.setServoAngle(13,120)
    servo.setServoAngle(10,120)
    servo.setServoAngle(31,120)
    servo.setServoAngle(18,60)
    servo.setServoAngle(21,60)
    servo.setServoAngle(27,60)

def pointFingers():
    servo=Servo.Servo()
    #move head out of the way
    servo.setServoAngle(HEAD_V,180)

    #position fingers
    servo.setServoAngle(FRONT_LEFT_KNEE,120)
    servo.setServoAngle(FRONT_LEFT_TIP,90)
    servo.setServoAngle(FRONT_LEFT_HIP,45)
    servo.setServoAngle(FRONT_RIGHT_KNEE,0)
    servo.setServoAngle(FRONT_RIGHT_TIP,90)
    servo.setServoAngle(FRONT_RIGHT_HIP,160)


    #position back Hips for stability
    servo.setServoAngle(CENTER_LEFT_HIP,60)
    servo.setServoAngle(CENTER_RIGHT_HIP,120)
    servo.setServoAngle(BACK_LEFT_HIP,60)
    servo.setServoAngle(BACK_RIGHT_HIP,120)
    #position legs
    servo.setServoAngle(CENTER_LEFT_KNEE,90)
    servo.setServoAngle(BACK_LEFT_KNEE,120)
    servo.setServoAngle(CENTER_RIGHT_KNEE,90)
    servo.setServoAngle(BACK_RIGHT_KNEE,60)
    servo.setServoAngle(CENTER_LEFT_TIP,120)
    servo.setServoAngle(BACK_LEFT_TIP,120)
    servo.setServoAngle(CENTER_RIGHT_TIP,60)
    servo.setServoAngle(BACK_RIGHT_TIP,60)

def standingPosition():
    print("Standing up")
    servo=Servo.Servo()
    try:
        
        servo.setServoAngle(15,90)
        servo.setServoAngle(12,90)
        servo.setServoAngle(9, 90)
        servo.setServoAngle(16,90)
        servo.setServoAngle(19,90)
        servo.setServoAngle(22,90)
        time.sleep(1)

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
    except KeyboardInterrupt:
        print ("\ninterrrupted")
    time.sleep(1)

if __name__ == '__main__':
    zeroPosition()
    standingPosition()
    zeroPosition()
    tipToes()
    jumpUp()