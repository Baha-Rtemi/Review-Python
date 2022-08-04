list = []

for i in range(3):
    s = float(input("What's Your Score ? "))
    list.append(s)
print(f"Your Scores Are : {list}")
print(f"Your Average : {sum(list) / len(list)}")
print()
print("####################")
print("####################")
print("Average: " + str(sum(list) / len(list)))
print(f"Average: {sum(list) / len(list)}")#When u use f no need to translate it to string
