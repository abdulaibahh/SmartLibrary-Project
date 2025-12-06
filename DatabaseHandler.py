import psycopg2
from config import DATABASE_CONFIG
from models import Book


class DatabaseHandler:
    def connect(self):
        return psycopg2.connect(DATABASE_CONFIG)

    def get_user_auth(self, email):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT m.MemberID, a.PasswordHash, m.Role, m.FirstName, m.LastName
            FROM MEMBERS m JOIN AUTHENTICATION a ON m.MemberID = a.MemberID
            WHERE m.Email = %s
        """, (email,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    def search_books(self, keyword="", genre=None, status=None):
        conn = self.connect()
        cur = conn.cursor()
        query = "SELECT BookID, Title, ISBN, Genre, Status FROM BOOKS WHERE 1=1"
        params = []
        if keyword:
            query += " AND (Title ILIKE %s OR ISBN ILIKE %s)"
            params += [f"%{keyword}%", f"%{keyword}%"]
        if genre and genre != "All":
            query += " AND Genre = %s"
            params.append(genre)
        if status and status != "All":
            query += " AND Status = %s"
            params.append(status)
        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Book(*row) for row in rows]

    def get_book(self, book_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT BookID, Title, ISBN, Genre, Status FROM BOOKS WHERE BookID=%s", (book_id,))
        r = cur.fetchone()
        cur.close()
        conn.close()
        return Book(*r) if r else None

    def borrow_book(self, book_id, member_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("UPDATE BOOKS SET Status='On Loan' WHERE BookID=%s AND Status='Available' RETURNING BookID",
                    (book_id,))
        if not cur.fetchone():
            conn.close()
            return False
        cur.execute(
            "INSERT INTO LOANS (BookID, MemberID, LoanDate, DueDate) VALUES (%s, %s, CURRENT_DATE, CURRENT_DATE + INTERVAL '14 days')",
            (book_id, member_id))
        conn.commit()
        cur.close()
        conn.close()
        return True

    def return_book(self, loan_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("UPDATE LOANS SET ReturnDate=CURRENT_DATE WHERE LoanID=%s AND ReturnDate IS NULL RETURNING BookID",
                    (loan_id,))
        row = cur.fetchone()
        if row:
            cur.execute("UPDATE BOOKS SET Status='Available' WHERE BookID=%s", (row[0],))
            conn.commit()
        cur.close()
        conn.close()
        return bool(row)

    def get_member_loans(self, member_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT l.LoanID, b.Title, l.LoanDate, l.DueDate, l.ReturnDate IS NULL
            FROM LOANS l JOIN BOOKS b ON l.BookID = b.BookID
            WHERE l.MemberID = %s ORDER BY l.LoanDate DESC
        """, (member_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_stats(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM BOOKS")
        total_books = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM MEMBERS WHERE Role='Member'")
        total_members = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM LOANS WHERE ReturnDate IS NULL")
        active_loans = cur.fetchone()[0]
        cur.close()
        conn.close()
        return total_books, total_members, active_loans

    def add_book(self, title, isbn, genre):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO BOOKS (Title, ISBN, Genre, Status, PublicationDate) 
            VALUES (%s, %s, %s, 'Available', CURRENT_DATE)
        """, (title, isbn, genre))
        conn.commit()
        cur.close()
        conn.close()

    def delete_book(self, book_id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM BOOKS WHERE BookID = %s", (book_id,))
        conn.commit()
        cur.close()
        conn.close()

    def create_user(self, first_name, last_name, email, role, hashed_password):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO MEMBERS (FirstName, LastName, Email, Role, JoinDate)
                VALUES (%s, %s, %s, %s, CURRENT_DATE) RETURNING MemberID
            """, (first_name, last_name, email, role))
            member_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO AUTHENTICATION (MemberID, PasswordHash)
                VALUES (%s, %s)
            """, (member_id, hashed_password))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Error creating user:", e)
            return False
        finally:
            cur.close()
            conn.close()
        return True

    def get_all_members(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT MemberID, FirstName, LastName, Email, Role 
            FROM MEMBERS 
            ORDER BY MemberID
        """)
        members = cur.fetchall()
        cur.close()
        conn.close()
        return members

    def delete_user(self, member_id):
        conn = self.connect()
        cur = conn.cursor()

        try:
            # 1. Check for active loans (Prevent deletion if member has active loans)
            cur.execute("SELECT count(*) FROM LOANS WHERE MemberID = %s AND ReturnDate IS NULL", (member_id,))
            active_loans_count = cur.fetchone()[0]

            if active_loans_count > 0:
                raise Exception(f"Member has {active_loans_count} active loan(s) and must return them first.")

            cur.execute("DELETE FROM AUTHENTICATION WHERE MemberID = %s", (member_id,))

            cur.execute("DELETE FROM MEMBERS WHERE MemberID = %s", (member_id,))

            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()