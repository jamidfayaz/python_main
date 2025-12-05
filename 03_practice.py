name=input("plaese enter your name\n")
print("good after noon",name)               #or
print(f"Good Afternoon {name}")   # by making it f string   or
print("good Afternoon" +name+ "hi")         #by addding +  


###printing dear +name+ you are selected at current date
from datetime import date
name=input("enter your name\n")

print("letter=")
print("dear",name)
print("you are selected")

# Get the current date
current_date = date.today()
print(current_date)


### str replace
name="jamid  fayaz"
s=name.find("  ")
print(s)
print(name.replace("  "," "))


 