people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

namenumber = input("Number of ? ")

if namenumber in people:
    print(f"The Number of {namenumber} is {people[namenumber]}.")

else:
    print(f"Sorry, The Number of {namenumber} is Not Exist.")