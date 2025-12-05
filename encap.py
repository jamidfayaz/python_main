class student():
    def __init__(self,name,grade):
            self.__name=name                    #__ makes private
            self.__grade=grade
        
    def get__name(self):
            print(self.__name)

    def set__age(self,age):
           if age<=18:
                print("not eligible")
           else:
                self.__age=age
                print(self.__age)
st_1=student("anayat",10)

st_1.get__name()
st_1.set__age(30)
#print(st_1.name)           #it will throw error because --name is private