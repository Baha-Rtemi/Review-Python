try:
    x = int(input("Give Me A Number! "))
except ValueError:
    print("That is not an int!")
    exit(1)

try:
    y = int(input("Give Me A Number! "))
except ValueError:
    print("That is not an int!")
    exit(1)

print(x / y)