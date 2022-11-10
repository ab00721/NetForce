from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force(dataList):
    hMag = 0
    vMag = 0
    for values in dataList:
        angleRad = radians(values[1])
        hMag += values[0] * cos(angleRad)
        vMag += values[0] * sin(angleRad)
        magnitude = round(sqrt((hMag ** 2) + (vMag ** 2)), 1)
        angle = round(degrees(atan2(vMag, hMag)), 1)
    return(magnitude, angle)
 
forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print("Magnitude and angle (degrees) of net force:", find_net_force(forces))



