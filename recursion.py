def fibo(n):
    if n<=1:
        return 1
    return fibo(n-1)+fibo(n-2)
terms=10
for i in range(terms):
    print(fibo(i),end='')


#now decimal to binary

def dec_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    else:
        return dec_to_binary(n // 2) + str(n % 2)

a = dec_to_binary(4)
print(a)


## decimal to hexa decimal
def hb(n):
    hexnum = "0123456789ABCDEF"
    # quotient=n//2
    # remainder=n%16
    if n<16:
        return hexnum[n]
    else:
        return hb(n//16)+hexnum[n%16]
a=hb(10)
print(a)