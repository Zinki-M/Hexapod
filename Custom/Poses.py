from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Servo
import time

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
    servo=Servo.Servo()
    print("Preparing jump")
    zeroPosition()
    print("Jumping up")
    servo.setServoAngle(14,90)
    servo.setServoAngle(11,90)
    servo.setServoAngle(8,90)
    servo.setServoAngle(17,90)
    servo.setServoAngle(20,90)
    servo.setServoAngle(23,90)
    servo.setServoAngle(13,90)
    servo.setServoAngle(10,90)
    servo.setServoAngle(31,90)
    servo.setServoAngle(18,90)
    servo.setServoAngle(21,90)
    servo.setServoAngle(27,90)
    time.sleep(1)


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