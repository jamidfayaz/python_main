###class Book 
books = []

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def add_book(self):
        books.append(self)
        print("Book added successfully")

    @staticmethod
    def remove_book(title):
        for book in books:
            if book.title == title:
                books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    @staticmethod
    def display():
        b = input("Enter book title: ")
        for book in books:
            if book.title == b:
                print(f"Title: {book.title}, Author: {book.author}")
                return
        print("Book not found")
    def ad():
        for i in books:
            print(i.title,i.author)

# Creating and adding books
b1 = Book("kashmiriyat", "mr taufeek")
b1.add_book()

b2 = Book("aqi", "aqib")
b2.add_book()
print(books)
Book.display()
Book.ad()