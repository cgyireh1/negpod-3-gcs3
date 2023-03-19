#!/usr/bin/python3
month = input("Enter the name of a month: ")

if month.lower() in ("january", "march", "may", "july", "august", "october", "december"):
    print(month.capitalize, "has 31 days")
elif month.lower() in ("april", "june", "september", "november"):
    print(month.capitalize, "has 30 days")
elif month.lower() == "february":
    print(month.lower, "has 28 or 29 days, depending on the year")
else:
    print("Invalid month name entered")
