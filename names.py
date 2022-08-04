import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Search For A Name? ")

if name in names:
    print(f"{name} is Found.")
    sys.exit(0)
else:
    print(f"{name} is Not Found.")
    sys.exit(1)