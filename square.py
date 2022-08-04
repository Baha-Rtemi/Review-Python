def square(x):
    return x * x

n = int(input("Square of: \n"))

for i in range(n):
    print(f"The Square of {i} is {square(i)}")