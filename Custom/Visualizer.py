
import ast
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, pi

def point_pos(x0, y0, d, theta):
    theta_rad = pi/2 - radians(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)

def readDistances():
    with open("sweeps.txt") as fily:
        data = fily.read()
         
    # reconstructing the data as a dictionary
    decoded = ast.literal_eval(data)
    return decoded

def convertDistances(distances):
    allPoints = []
    for pos, angle, dists in distances:
        scanPoints = []
        numDists = len(dists)
        #bangle is center angle
        startAngle = angle - numDists//2
        #add 15cm to distance because of robot size
        startPoint = point_pos(pos[0],pos[1],15,angle)
        for i in range(numDists):
            scanPoints.append(point_pos(startPoint[0],startPoint[1],dists[i]+15,startAngle+i))
        allPoints.append((pos,angle,scanPoints))
    return allPoints


def visualizeDistances(distances):
    points = convertDistances(distances)
    print(points)
    legend = []
    for pos,angle,scanPoints in points:
        plt.scatter(*zip(*scanPoints))
        legend.append(str(pos)+", "+str(angle)+"°")
    plt.legend(legend, loc="upper left")
    plt.show()

if __name__ == "__main__":
    visualizeDistances(readDistances())