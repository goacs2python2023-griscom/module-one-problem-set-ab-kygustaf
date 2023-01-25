# Kyle Gustafson
# 1/24/22
# Elizabeth Griscom
# This program calculates the cost of a road trip

mpg = int(input("Fuel efficiency in miles per gallon: "))
distance = int(input("Miles driven: "))
cost = int(input("Cost of gas in dollars: "))

def CostCalculator():
    totalcost = (distance/mpg)*cost
    return round(totalcost, 2)

print(str(CostCalculator()))