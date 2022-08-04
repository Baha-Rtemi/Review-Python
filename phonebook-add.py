import csv

Name = input('What is Your Name? ')
Number = input('What is Your Phone Number? ')

file = open("phonebook.csv", "a")
write = csv.writer(file)
write.writerow([Name, Number])
file.close()
# csv.writer(open("phonebook.csv", "a")).writerow([Name, Number])
# file.close()

# Pythonic Way 
# with open("phonebook.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow((name, number))
# 
# and when u use (( with )) no need to write (( file.close() ))