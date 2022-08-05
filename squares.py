from functions import square

n = int(input("Which Number you want Square of ? \n"))

for i in range(n + 1):
    print(f"The Square of Number {i} is {square(i)}")