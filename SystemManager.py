import bcrypt
from DatabaseHandler import DatabaseHandler
from models import Member, Librarian


class SystemManager:
    def __init__(self):
        self.db = DatabaseHandler()
        self.loggedInUser = None

    def verifyLogin(self, email, password):
        data = self.db.get_user_auth(email)
        if not data:
            return False
        mid, hash_pw, role, first, last = data
        if bcrypt.checkpw(password.encode(), hash_pw.encode()):
            self.loggedInUser = (Librarian if role == 'Librarian' else Member)(mid, email, first, last)
            self.loggedInUser.user_id = mid
            return True
        return False

    def searchBooks(self, keyword="", genre="All", status="All"):
        return self.db.search_books(keyword, genre, status)

    def borrowBook(self, book_id):
        if self.db.get_member_loans(self.loggedInUser.user_id):
            active = [l for l in self.db.get_member_loans(self.loggedInUser.user_id) if l[4]]
            if len(active) >= 3:
                return "Maximum 3 books allowed"
        if self.db.borrow_book(book_id, self.loggedInUser.user_id):
            return "Book borrowed successfully!"
        return "Book not available"

    def returnBook(self, loan_id):
        if self.db.return_book(loan_id):
            return "Book returned successfully!"
        return "Error returning book"

    def getMyLoans(self):
        return self.db.get_member_loans(self.loggedInUser.user_id)

    def getStats(self):
        return self.db.get_stats()

    def delete_member(self, member_id):
        """Forwards the member deletion request to the DatabaseHandler."""
        return self.db.delete_user(member_id)
