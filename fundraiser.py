# Kyle Gustafson
# 1/24/22
# Elizabeth Griscom
# This program calculates how much money a fundraiser raised

def profit():
    tickets = int(input("How many tickets were sold?: "))
    return (tickets*5)-50

print(str(profit()))