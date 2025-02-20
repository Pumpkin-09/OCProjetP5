class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []
     
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
    
    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
    
    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
    
    def available_books(self):
        print("Voici les livres disponible:")
        for book in self.books:
            print(book.title)
            
    
    def borrowed_books(self):
        print("Voici les livres emprunter:")
        for book in self.borrow_books:
            print(book.title)

    # Ajouter les méthodes ici

livre1 = Book("titre1", "author1", "year1")
livre2 = Book("titre2", "author2", "year2")
livre3 = Book("titre3", "author3", "year3")

library = Library()

library.add_book(livre1)
library.add_book(livre2)
library.add_book(livre3)

library.available_books()
library.borrowed_books()
print("---\n")
library.borrow_book(livre1.title)
library.available_books()
library.borrowed_books()
print("---\n")
library.return_book(livre1.title)
library.available_books()
print("---")
library.borrowed_books()
print("---\n")