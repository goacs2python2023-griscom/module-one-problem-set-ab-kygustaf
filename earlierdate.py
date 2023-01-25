# Kyle Gustafson
# 1/23/22
# Elizabeth Griscom
# This program determines which of 2 dates occurs earlier.

date1 = {
    "year" : int(input("year of first date: ")),
    "month" : int(input("Month of first date: ")),
    "day" : int(input("Day of first date: "))
}

date2 = {
    "year" : int(input("year of second date: ")),
    "month" : int(input("Month of second date: ")),
    "day" : int(input("Day of second date: "))
}

def EarlierDate():
    if date1["year"] < date2["year"]:
        return("The first date is earlier")
    elif date2["year"] < date1["year"]:
        return("The first date is later")
    elif date1["year"] == date2["year"]:
        if date1["month"] < date2["month"]:
            return("The first date is earlier")
        elif date1["month"] > date2["month"]:
            return("The first date is later")
        elif date1["month"] == date2["month"]:
            if date1["day"] < date2["day"]:
                return("The first date is earlier")
            elif date1["day"] > date2["day"]:
                return("The first date is later")
            else:
                return("Those are the same date!")


print(EarlierDate())