d={"aqib":"yousuf",
   "jamid":"fayaz",
    "ananyat":"naik",
    0:"harry"
}
print(d)
print(type(d))
print(d.get("aqib"))         #it does not give error when key not present
print(d["aqib"])             #it can give error 
# print(d.clear())
print(d.items())
print(d.keys())  #or print(d["keys"])      no duplicate keys
print(d.values())
print(d.pop("jamid"))
print(d.update({"inn":"pin"}))
# print(d.values())
#print(del d["aqib"])
print(d.copy())
print(d)