#Recursion is that where function calls itself 

def factorial(n):
    if n==1 or n==0:
        return 1
    return n* factorial(n-1)
n=int(input("enter any no"))
print(f"the fact is {factorial(n)}")



# #practice

def greater():
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("entr any no"))
b=int(input("entr any no"))
c=int(input("entr any no"))
print(f"the bigger no is {greater()}")

# def sum(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     return n+sum(n-1)
# n=int(input("enter "))
# print(sum(n))


###fibonacci series 
def fibo(n):
    if n<=1:
        return 1
    return fibo(n-1)+fibo(n-2)
terms=10
for i in range(terms):
    print(fibo(i),end=' ')




# n=int(input("enter any number"))
# r=0
# l=len(str(n))
# for i in range (0,4):
#         n=(n//2)
#         r=str(n%2)
#         print(r,end=" ")


    def dec_to_hex(n):
     hex_chars = "0123456789ABCDEF"
    
    if n < 16:
        return hex_chars[n]
    
        return dec_to_hex(n // 16) + hex_chars[n % 16]

# Example
num = int(input("Enter a number: "))
print("Hexadecimal:", dec_to_hex(num))





def dec_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return dec_to_binary(n // 2) + str(n % 2)

# Example
num = int(input("Enter a number: "))
print("Binary:", dec_to_binary(num))






def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print Fibonacci series
num = int(input("Enter how many terms: "))

print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")
