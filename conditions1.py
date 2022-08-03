c = input("Are You Agree ? ")

if c == 'yes' or c == "y":
    print("yes I'm Agree.")
if c.lower() in ['y', 'yes']:
    print("Yes I'm Agree.")
if c.lower() in ['n', 'no']:
    print("No I'm Not Agree.")