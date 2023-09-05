# find the largest number in list
names = [30, 40, 20, 1, 3, 10, 16, 22, 55, 2]
print(names)
names.sort()
print(names)
# [-1] indexes the final object in the list
print(names[-1])

# you could also reverse the list and have it pull index [0]
names = [30, 40, 20, 1, 3, 10, 16, 22, 55, 2]
print(names)
names.sort()
print(names)
names.reverse()
print(names)
# [-1] indexes the final object in the list
print(names[0])
