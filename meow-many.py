s = int(input("How many time do you want say {{ Hello! }}  "))

def sayit():
    manytime(s)

def manytime(a):
    for i in range(a):
        print(f"{i + 1}  Hello!")

sayit()


# def main():
#     meow(3)
#
# def meow(n):
#     for i in range(n):
#         print("meow")
#
# main()