#tuples are immutable
# t1(1,)                  #if single element add , to how interpriter
# t2()                    #empty tuple
t=(1,2,2,3,"jamid")
print(type(t))
print(t)
no=t.count(2)               #occurance of element
print(no)

s=t.index(3)
print(s)

t3=t*2
print(t3)

print(len(t3))