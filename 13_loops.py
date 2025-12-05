###factorial of any number
n=int(input("enter the no:"))
product=1
for i in range(1,n+1):
    product=product*i
print(f"the fact o {n}is {product}")

#program for finding the sun of series upto n number
sum=0
i=0
while(i<n):
    sum += i
    i += 1
print(f"the sum is {sum}")

#program for printing even nos.
for i in range(0,n+1,2):
    print(i)


##printing the shapes
n=int(input("enter lines to print"))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

n=int(input("enter lines to print"))
for i in range(1,n+1):
    if (i==1) or (i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")

#program for printing tables
n=int(input("rnter"))
i=10
for i in range(0,10):
    print(F"{n}x{i}={n*i}")