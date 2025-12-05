numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)

print(list(result))  # [2, 4, 6, 8]


names = ["jamid", "fayaz", "python"]
upper_names = list(map(lambda s: s.upper(), names))

print(upper_names)
# ['JAMID', 'FAYAZ', 'PYTHON']


a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))

print(result)   # [5, 7, 9]



nums = [10, 20, 30]
result = map(str, nums)

print(list(result))



#lambda
square = lambda x: x * x
print(square(6))


#filter
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
#Output:
#[2, 4, 6]



names = ["Ram", "Aman", "Ali", "John"]

result = list(filter(lambda x: len(x) > 3, names))
print(result)


#reduce
from functools import reduce

nums = [2, 3, 4]

result = reduce(lambda x, y: x * y, nums)
print(result)
