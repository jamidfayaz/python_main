# n=int(input("enter any no."))
# sum=0
# fact=1
# for i in range(1,n+1):
#     fact=1
#     for j in range (1,i+1):
#         fact=fact*j
#     sum=sum+fact
# print(sum)

n=5
for i in range (1,n+1):
    for j in range (1,i+2):
        print(" "*(n-i))
    print("*"*i,end="")
#     *
#    ***
#   *****
#  *******
# *********
