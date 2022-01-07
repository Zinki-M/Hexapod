from os import sys, path
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))),"Server"))
import Servo


def zeroPosition():
    Servo.servo_installation_position()




if __name__ == '__main__':
    zeroPosition()
