# def func():
#     print("hello world")

# func()      #function call
# print("end")

#function with arg
def hello(name,ending):
    print("hey"+name)
    print(ending)
hello("jamid","thankyou")
hello("aqi","thankyou")



# def hello(name,ending):
#     print("hey"+name)
#     print(ending)
#     return 'ended' #or anything like avg value
# a=hello("jamid","thankyou")
# # hello("aqi","thankyou")
# print(a)



# def hello(name,ending="thank you"):    #default arg
#     print("hey"+name)
#     print(ending)
#     return 'ended' #or anything like avg value
# a=hello("jamid")
# # hello("aqi","thankyou")
# print(a)
# hello("jamid","thanks")     #if arg available then prints it if notg then default value


##functions with named arguments
def avg(num1,num2,num3):
    print((num1+num2+num3)/3)
avg(num1=1,num2=3,num3=4)


