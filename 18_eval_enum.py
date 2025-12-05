for index, item in enumerate(fruits, start=1):
    print(index, item)



fruits = ["apple", "banana", "mango"]

for index, item in enumerate(fruits):
    print(index, item)


#bad technique
for i in range(len(fruits)):
    print(i, fruits[i])

#good technique
for i, fruit in enumerate(fruits):
    print(i, fruit)
