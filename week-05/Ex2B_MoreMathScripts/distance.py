# Name: Leon Poulson
# Date: 5/8/26
# Instructor: Deodat
# Calulate The distance between two points

import math

x1 = eval(input("Your first X cord: "))
x2 = eval(input("Your Secound X cord: "))
y1 = eval(input("Your first Y cord: "))
y2 = eval(input("Your Secound Y cord: "))

x_calulation = (x2 - x1)**2
y_calulation = (y2 - y1)**2
x_and_y = x_calulation + y_calulation
distance = math.sqrt(x_and_y)

print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance}")