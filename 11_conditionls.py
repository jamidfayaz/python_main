#eligible for voting or not
a=int(input("enter your age: "))

if a>=18:
    print("eligible for voting")
    print("hess karzi modi chui nachan")
elif(a<=0):
    print("age cant be 0 or negative")
else:
    print("not eligible")

print("yes") if a>=18 else print("no")     #same
print(("no","yes")[a>=18])                 #same


####even no.
if(a%2==0):
    print("no.is even")
else:
    print("odd")            #end of if 1

###eligible for voting or not
if a>=18:
    print("eligible for voting")
    print("hess karzi modi chui nachan")
elif(a<=0):
    print("age cant be 0 or negative")
else:
    print("not eligible")         # end of if 2

##greater number
n1=int(input("enter 1 no"))
n2=int(input("enter 1 no"))
n3=int(input("enter 1 no"))
n4=int(input("enter 1 no"))
if (n1>=n2 and n3,n4):
    print("n1 is greater")
elif(n2>=n1,n3,n4):
    print("n2 is greater")            #use and operators
elif(n3>n1,n2,n4):
    print("no 3")
elif(n4>n1,n2,n3):
    print("no.4")

  

###pass or fail
s1=int(input("marks 1:"))
s2=int(input("marks 2:"))
s3=int(input("marks 3:"))
s4=(100)*(s1+s2+s3)/300             #percent
if (s4>=40 and s1>=33 and s2>= 33 and s3>=33):
    print("pass",s4)
else:
    print("fail",s4)

###program for checking spam or not using list
w=input("enter any word")
l=["set","get"]
for w in l:
    print("spam")

w=input("enter any word")
if (len(w)<10):
    print("yes")
else:
    print("no")


##program for checking spam or nor from a word
p1 = "hello"
p2 = "hi"
word = input("Enter any word: ")

if (p1 in word) or (p2 in word):
    print("spam")
else:
    print("notspam")



#program for checking if word is in a list or not
list=["jamid","aqib","fayaz"]
word=input("enter any word")
if(word in list):
    print ("yes")
else:
    print("no")


#program for checking if a word in the input word or not
word = input("Enter any word: ")
if ("jamid".lower() in word.lower()):
    print('yes')
else:
    print("No")

    