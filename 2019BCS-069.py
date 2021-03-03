import math
from operator import add

a=int(input("Enter the x-coordinate of the point: "))
b=int(input("Enter the y-coordinate of the point: "))
c=int(input("Enter the z-coordinate of the point: "))

point = [a, b, c]

axes = list(input("Enter axes about which to rotate(in x,y,z with spaces): ").split(" "))

print(point)
print(axes)
for i in axes:
    new_points = []
    print("Rotation about " + i + "-axis(in degrees),enter in negative value for ClockWise rotation: ")
    degrees = math.radians(int(input()))
    if i=='x':
        new_points.append(point[0])
        new_points.append((point[1]*math.cos(degrees)) - point[2]*math.sin(degrees))
        new_points.append((point[1]*math.sin(degrees)) + point[2]*math.cos(degrees))
    if i=='y':
        new_points.append((point[0]*math.cos(degrees)) - point[2]*math.sin(degrees))
        new_points.append(point[1])
        new_points.append((point[0]*math.sin(degrees)) + point[2]*math.cos(degrees))
    if i=='z':
        new_points.append((point[0]*math.cos(degrees)) - point[1]*math.sin(degrees))
        new_points.append((point[0]*math.sin(degrees)) + point[1]*math.cos(degrees))
        new_points.append(point[2])

    point = new_points

print("new coordinates after rotations = ")
print(point)

transx = int(input("translation about x-axis:"))
transy = int(input("translation about y-axis:"))
transz = int(input("translation about z-axis:"))

trans=[transx, transy, transz]

final = list(map(add, point, trans))

print(final)