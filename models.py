
from datetime import date

class User:
    def __init__(self, user_id, email, first_name, last_name, role):
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

class Member(User):
    def __init__(self, user_id, email, first_name, last_name):
        super().__init__(user_id, email, first_name, last_name, 'Member')

class Librarian(User):
    def __init__(self, user_id, email, first_name, last_name):
        super().__init__(user_id, email, first_name, last_name, 'Librarian')

class Book:
    def __init__(self, book_id, title, isbn, genre, status='Available', publication_date=None):
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.genre = genre
        self.status = status
        self.publication_date = publication_date

    def isAvailable(self):
        return self.status == 'Available'