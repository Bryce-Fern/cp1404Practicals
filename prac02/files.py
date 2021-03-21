list_of_names = open("name.txt", 'w')
name = input("What is your name?: ")
print(name, file=list_of_names)
list_of_names.close()

open_name = open("name.txt", "r")
name = open_name.read().strip()
open_name.close()
print("Your name is", name)

numbers = open("numbers.txt", "r")
n1 = int(numbers.readline())
n2 = int(numbers.readline())
numbers.close()
print(n1 + n2)

numbers = open("numbers.txt", "r")
allnumbers = 0
for line in numbers:
    number = int(line)
    total += number
numbers.close()
print(allnumbers)