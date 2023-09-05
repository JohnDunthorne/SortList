# find the largest number in list
print("method using negative indexing")
names = [30, 40, 20, 1, 3, 10, 16, 22, 55, 2]
print(names)
names.sort()
print(names)
# [-1] indexes the final object in the list
print(names[-1])

# you could also reverse the list and have it pull index [0]
print("method using reverse")
names = [30, 40, 20, 1, 3, 10, 16, 22, 55, 2]
print(names)
names.sort()
print(names)
names.reverse()
print(names)
# [-1] indexes the final object in the list
print(names[0])

# you can do this with a for loop
print("method using for loop")
names = [30, 40, 20, 1, 3, 10, 16, 22, 55, 2]
max_number = names[0]
for number in names:
    if number > max_number:
        max_number = number
print(max_number)
