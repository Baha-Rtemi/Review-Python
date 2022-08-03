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

z = x / y

print(f"{x} / {y} = Int z : {z}")

print(f"{x} / {y} = Float z : {z:.5f}")