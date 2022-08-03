# while you can have two or more of the same elements within a list/tuple,
# a set will only store each value once. 
s = set()

s.add(100)
s.add(200)
s.add(300)

print(f"The set is {s} and the set has {len(s)} eleements.")

s.add(100)

print(f"The set is {s} and the set has {len(s)} eleements.")

s.remove(100)

print(f"The set is {s} and the set has {len(s)} eleements.")
