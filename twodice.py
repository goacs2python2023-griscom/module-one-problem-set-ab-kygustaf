# Kyle Gustafson
# 1/23/22
# Elizabeth Griscom
# This program rolls two dice and determines if the sum of those dice equals some preset values.

import random
def SumDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    sum = int(dice1) + (dice2)

    if sum == 6 or sum == 7 or sum == 8:
        return "win"
    else:
        return "lose"

print(SumDice())