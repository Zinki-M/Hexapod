from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Servo


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



if __name__ == '__main__':
    zeroPosition()
    curledPosition()