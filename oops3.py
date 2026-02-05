#Create a single inheritance program for a Library system.
#a.Create a parent class named Book with:
# Parent Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    
    def display_book_details(self):
        print("Title is", self.title)
        print("Author is", self.author)



class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)   # Call parent constructor
        self.issued_to = issued_to
        self.issued_date = issued_date


    def display_issued_book_details(self):
        self.display_book_details()   # Call parent method
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)
issued_book = IssuedBook("Python Basics", "Guido van Rossum", "Madhushree", "04-02-2026")
issued_book.display_issued_book_details()
