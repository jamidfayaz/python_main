print(5 + 3)        # 8  → Addition
print("A" + "B")    # AB → String concatenation
# here same operator but different behavior




class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):          # Overriding
        print("Dog barks")

class Cat(Animal):
    def sound(self):          # Overriding
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()   # Animal makes a sound
d.sound()   # Dog barks
c.sound()   # Cat meows




class India:
    def capital(self):
        print("New Delhi")

class USA:
    def capital(self):
        print("Washington D.C.")

countries = [India(), USA()]

for country in countries:
    country.capital()