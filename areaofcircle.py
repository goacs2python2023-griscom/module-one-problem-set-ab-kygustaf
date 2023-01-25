# Kyle Gustafson
# 1/24/22
# Elizabeth Griscom
# This program calculates the area of a circle

import math

def SquareCalc():
    num = int(input("Enter a number: "))
    return num**2

def AreaCircle():
    area = SquareCalc()*math.pi
    return area

print(str(AreaCircle()))