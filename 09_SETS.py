# set=set()       #for empty set we use () not this {} because empty dict is also in{}
# set.add(2)
# set.add(3)
# print(set)

s={1,2,5,7,4,"jamid"}
s.add(34)                       #no order no index no change in items no duplicate
print(s)

print(len(s))
print(s.remove(1))
s.pop()
s.clear()

s1={1,2,3}
s2={4,5,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print({1}.issubset(s1))