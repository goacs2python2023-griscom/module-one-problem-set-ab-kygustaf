# Kyle Gustafson
# 1/24/22
# Elizabeth Griscom
# This program determines how many busses are needed to transport a given number of students

NumStudents = int(input("Number of students: "))

def busses(students):
    if NumStudents % 52 == 0:
        return int(NumStudents / 52)
    else:
        return int(NumStudents / 52) + 1

print(busses(NumStudents))