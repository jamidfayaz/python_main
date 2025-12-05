p1 = "hello"
p2 = "hi"
word = input("Enter any word: ")

if (p1 in word) or (p2 in word):
    print("spam")
else:
    print("notspam")

