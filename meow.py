def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

main()

# We might also see examples that call a main function with:
# if __name__ == "__main__":
    # main()
# This solves problems with including our code in libraries,
# but we won’t need to consider that yet, so we can simply call main().