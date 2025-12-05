name="aqib soeb"
print(len(name))
print(name.endswith("soeb"))
print(name.startswith("soeb"))             #   starts and ends with check    case sensitive
print(name.startswith("aqib"))

print(name.capitalize())              #  capital first character

print("aqib".upper())
                 
                 
                                               ## lower and upper case ways
name1='AQIB'
cap=name1.lower()
print(cap)

###find and replace

s="hi my name is jamid"                         #  title give first letter capital
print(s.title())

print(name.find("s"))                            # finds index of word
 
s=name.replace("aqib","jamidd")                   #replace 
print(s)