# Kyle Gustafson
# 1/23/22
# Elizabeth Griscom
# This program determines if the word DAD can be spelled based on the letter values of 3 two-sided cards.


front = input("Enter the letters on the top sides of your cards; all caps, in succession, with no spaces in between: ")
back = input("Enter the letters on the bottom sides of your cardsall caps, in succession, with no spaces in between: ")

# The word we are looking for in this program is "DAD". A more complicated program would ask for a word from the user.
countA = 0
countD = 0

for letter in front:
    if letter == "D":
        countD += 1
    elif letter == "A":
        countA += 1

for letter in back:
    if letter == "D":
        countD += 1
    elif letter == "A":
        countA += 1


if countA >= 1 and countD >=2:
    print("yes")
else: 
    print("no")
