class Person:
    def show(self):
        print("I am a person.")

class Student(Person):
    def show(self):
        super().show()   # calling parent method
        print("I am a student.")
        print("i am aqib")

s = Student()
s.show()

    
#adding new methods to a child class
class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class Manager(Employee):
    def approve_leave(self):
        print(f"{self.name} approved a leave request.")

m = Manager("Rahul", 50000)
m.work()
m.approve_leave()


#Multilevel inheritence

class A:
    def method1(self):
        print("Method of A")

class B(A):
    def method2(self):
        print("Method of B")

class C(B):
    def method3(self):
        print("Method of C")

obj = C()
obj.method1()
obj.method2()
obj.method3()

# Constructor Inheritance + Methods

       
class Shape:
    def _init_(self, color):
        print("shape")
        self.color = color

    def show_color(self):
        print("Color:", self.color)

class Rectangle(Shape):
    def _init_(self, color, width, height):
        print("constructor of rectangle")
        super()._init_(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class square(Rectangle):
    def _init_(self, color, width, height):
        print("square")
        super()._init_(color, width, height)

# r = Rectangle("Blue", 5, 4)
p = square("red", 12, 56)
# r.show_color()
# print("Area:", r.area())