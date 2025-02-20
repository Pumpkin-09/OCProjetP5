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
        print("Voici les livres emprintés:")
        for book in self.borrow_books:
            print(book.title)

    # Ajouter les méthodes ici
