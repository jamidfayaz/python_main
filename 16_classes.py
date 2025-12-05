class Employee:
    language = "py"
    salary = 120000

jamid = Employee()
jamid.name="jam"
print(jamid.name, jamid.language)

class Employee:
    language = "py"
    salary = 120000

aqib = Employee()
aqib.name= "aqii"   #obj attribute or instance attribute
print(aqib.name, aqib.language)

#here name is the object attribute and lang and salary are the class attribute


### instance vs class attribute

class Employee:
    language = "py"
    salary = 120000

jamid = Employee()
jamid.language="js"
print(jamid.language, jamid.language)   ## it will give us js because instance attribute has more prefrence than att


#### self

class Employee:
    language = "py"
    salary = 120000

    def getinfo(self):
        print(f"the lang is {self.language}.The sal is {self.salary}")

jamid = Employee()
jamid.name="jam"
print(jamid.name, jamid.language)
jamid.getinfo()         #this gets converted into -->Employee.getinfo(jamid)  jamid acts as self


