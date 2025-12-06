from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from SystemManager import SystemManager
import bcrypt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SmartLibrary - Limkokwing University")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(900, 600)
        self.system = SystemManager()
        self.setStyleSheet("""
            /* Global */
            QMainWindow {
                background: #0f1115;
                color: #E6EEF3;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel { color: #6082B6; }
            /* Header labels */
            QLabel[role="hero"] {
                color: #d7c6ff;
            }
            /* Buttons */
            QPushButton {
                background: #1b1d23;
                color: #E6EEF3;
                border: 1px solid #23252b;
                border-radius: 10px;
                padding: 8px 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #24262c;
            }
            QPushButton#primary {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #7f6bff, stop:1 #5a4cf1);
                color: white;
                border: none;
                font-weight: 700;
            }
            QPushButton#primary:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6b5bee, stop:1 #4a3fe0);
            }
            QPushButton#returnBtn {
                background: #27ae60;
                color: white;
                padding: 8px 16px;
                border-radius: 8px;
                font-weight: 600;
            }
            QPushButton#returnBtn:hover { background: #22a85a; }
            QPushButton#red {
                background: #e74c3c;
                color: white;
            }
            QPushButton#red:hover { background: #d73b2b; }
            /* Sidebar */
            QWidget#sidebar {
                background: #0d0f13;
                border-right: 1px solid #212327;
            }
            QPushButton.sidebarBtn {
                background: transparent;
                color: #cfd8e6;
                text-align: left;
                padding-left: 18px;
                border: none;
                font-size: 14px;
                height: 44px;
                border-radius: 8px;
            }
            QPushButton.sidebarBtn:hover {
                background: rgba(127,107,255,0.12);
                color: #efeefe;
            }
            QPushButton.sidebarBtn[active="true"] {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6f5bff, stop:1 #5a4cf1);
                color: white;
                font-weight: 700;
            }
            /* Inputs */
            QLineEdit, QComboBox, QTextEdit {
                background: #0f1115;
                color: #E6EEF3;
                padding: 10px;
                border-radius: 10px;
                border: 1px solid #232429;
            }
            QLineEdit:hover, QComboBox:hover {
                border: 1px solid #6f5bff;
            }
            /* GroupBox */
            QGroupBox {
                font-weight: bold;
                color: #bfb6ff;
                border: 1px solid #232429;
                border-radius: 12px;
                margin-top: 12px;
                background: transparent;
                padding: 8px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px;
                color: #d7c6ff;
                background: transparent;
            }
            /* Tables */
            QTableWidget {
                background: #0f1115;
                border: 1px solid #222426;
                gridline-color: #1b1d20;
                color: #E6EEF3;
                selection-background-color: rgba(127,107,255,0.16);
                selection-color: white;
                border-radius: 8px;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7f6bff, stop:1 #5a4cf1);
                color: white;
                padding: 10px;
                font-weight: 700;
                border: none;
            }
            QTableWidget QTableCornerButton::section {
                background: transparent;
                border: none;
            }
            /* Tabs */
            QTabWidget::pane { border: none; background: transparent; }
            QTabBar::tab { background: transparent; color: #cfd8e6; padding: 8px 12px; border-radius: 8px; }
            QTabBar::tab:selected { background: #6f5bff; color: white; }
            /* Scrollbars - subtle */
            QScrollBar:vertical {
                background: transparent;
                width: 10px;
                margin: 10px 0 10px 0;
            }
            QScrollBar::handle:vertical {
                background: #27282b;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line, QScrollBar::sub-line { height: 0; }
        """)
        self.showLogin()

    def make_scrollable(self, widget):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidget(widget)
        return scroll

    def showLogin(self):
        w = QWidget()
        l = QVBoxLayout()
        l.setAlignment(Qt.AlignCenter)
        l.setSpacing(15)
        title = QLabel("SMARTLIBRARY")
        title.setProperty("role", "hero")
        title.setFont(QFont("Segoe UI", 40, QFont.Bold))
        title.setStyleSheet("color: #d7c6ff;")
        title.setAlignment(Qt.AlignCenter)
        sub = QLabel("Limkokwing University Sierra Leone")
        sub.setFont(QFont("Segoe UI", 14))
        sub.setAlignment(Qt.AlignCenter)
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setFixedWidth(350)
        self.pwd = QLineEdit()
        self.pwd.setPlaceholderText("Password")
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.setFixedWidth(350)
        login_btn = QPushButton("LOGIN")
        login_btn.setFixedSize(350, 50)
        login_btn.setFont(QFont("Segoe UI", 16, QFont.Bold))
        login_btn.setObjectName("primary")
        login_btn.clicked.connect(self.login)
        l.addStretch()
        l.addWidget(title)
        l.addWidget(sub)
        l.addWidget(self.email)
        l.addWidget(self.pwd)
        l.addWidget(login_btn)
        l.addStretch()
        w.setLayout(l)
        self.setCentralWidget(w)

    def login(self):
        if self.system.verifyLogin(self.email.text(), self.pwd.text()):
            self.showDashboard()
        else:
            QMessageBox.critical(self, "Error", "Invalid credentials!")

    def showDashboard(self):
        central = QWidget()
        main = QVBoxLayout(central)
        main.setContentsMargins(15, 15, 15, 15)
        main.setSpacing(15)
        # Top header
        header = QLabel(f"Welcome, {self.system.loggedInUser.first_name} {self.system.loggedInUser.last_name}")
        header.setFont(QFont("Segoe UI", 28, QFont.Bold))
        header.setStyleSheet("color: #d7c6ff;")
        header.setAlignment(Qt.AlignLeft)
        role = QLabel(f"Role: {self.system.loggedInUser.role}")
        role.setAlignment(Qt.AlignRight)
        logout = QPushButton("Logout")
        logout.clicked.connect(self.showLogin)
        logout.setFixedHeight(36)
        top = QHBoxLayout()
        top.addWidget(header)
        top.addStretch()
        top.addWidget(role)
        top.addWidget(logout, alignment=Qt.AlignRight)
        # ==== Sidebar (left) ====
        sidebar_widget = QWidget()
        sidebar_widget.setObjectName("sidebar")
        sidebar_layout = QVBoxLayout(sidebar_widget)
        sidebar_layout.setContentsMargins(12, 12, 12, 12)
        sidebar_layout.setSpacing(6)

        def sidebar_button(text, page_key):
            b = QPushButton(text)
            b.setProperty("active", False)
            b.setObjectName("sidebarBtn")
            b.setProperty("class", "sidebarBtn")
            b.setFixedHeight(44)
            b.setStyleSheet("")
            b.clicked.connect(lambda _, key=page_key, btn=b: self._onSidebarClicked(key, btn))
            b.setProperty("sidebarBtn", True)
            b.setProperty("active", False)
            b.setProperty("page", page_key)
            return b

        self.btn_catalog = sidebar_button("Book Catalog", "catalog")
        self.btn_loans = sidebar_button("My Loans", "loans")
        self.btn_summary = sidebar_button("Dashboard Summary", "summary")
        self.btn_clubs = sidebar_button("Book Clubs", "clubs")
        sidebar_layout.addWidget(self.btn_catalog)
        sidebar_layout.addWidget(self.btn_loans)
        sidebar_layout.addWidget(self.btn_summary)
        sidebar_layout.addWidget(self.btn_clubs)

        if self.system.loggedInUser.role == 'Librarian':
            self.btn_admin = sidebar_button("Admin Panel", "admin")
            sidebar_layout.addWidget(self.btn_admin)
        else:
            self.btn_admin = None
        sidebar_layout.addStretch()
        self.stack = QStackedWidget()
        self.pages = {
            "catalog": self.make_scrollable(self.catalogTab()),
            "loans": self.make_scrollable(self.loansTab()),
            "summary": self.make_scrollable(self.summaryTab()),
            "clubs": self.make_scrollable(self.bookClubTab())
        }
        if self.system.loggedInUser.role == 'Librarian':
            self.pages["admin"] = self.make_scrollable(self.adminTab())
        for key, widget in self.pages.items():
            self.stack.addWidget(widget)
        self.switchPage("catalog")
        self._setActiveSidebarButton(self.btn_catalog)
        content_layout = QHBoxLayout()
        content_layout.addWidget(sidebar_widget, 1)
        content_layout.addWidget(self.stack, 6)
        main.addLayout(top)
        main.addLayout(content_layout)
        self.setCentralWidget(central)

    def _onSidebarClicked(self, page_key, btn):

        for b in [getattr(self, 'btn_catalog', None), getattr(self, 'btn_loans', None),
                  getattr(self, 'btn_summary', None), getattr(self, 'btn_clubs', None),
                  getattr(self, 'btn_admin', None)]:
            if b is not None:
                self._setInactiveSidebarButton(b)
        self._setActiveSidebarButton(btn)
        self.switchPage(page_key)

    def _setActiveSidebarButton(self, btn):
        if not btn:
            return
        btn.setProperty("active", True)
        btn.style().unpolish(btn)
        btn.style().polish(btn)
        btn.update()

    def _setInactiveSidebarButton(self, btn):
        if not btn:
            return
        btn.setProperty("active", False)
        btn.style().unpolish(btn)
        btn.style().polish(btn)
        btn.update()

    def switchPage(self, page_name):
        widget = self.pages.get(page_name)
        if widget:
            self.stack.setCurrentWidget(widget)

    def catalogTab(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setSpacing(15)
        search = QHBoxLayout()
        self.search_in = QLineEdit()
        self.search_in.setPlaceholderText("Search by title, ISBN or genre...")
        genre = QComboBox()
        genre.addItems(["All", "Technical", "Sci-Fi", "Classic", "Dystopian"])
        status = QComboBox()
        status.addItems(["All", "Available", "On Loan"])
        btn = QPushButton("Search")
        btn.setObjectName("primary")
        btn.clicked.connect(self.refreshCatalog)
        search.addWidget(self.search_in)
        search.addWidget(QLabel("Genre:"))
        search.addWidget(genre)
        search.addWidget(QLabel("Status:"))
        search.addWidget(status)
        search.addWidget(btn)
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "ISBN", "Genre", "Status", "Action"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.verticalHeader().setDefaultSectionSize(50)
        l.addLayout(search)
        l.addWidget(self.table)
        self.refreshCatalog()
        return w

    def refreshCatalog(self):
        books = self.system.searchBooks(self.search_in.text().strip() if hasattr(self, 'search_in') else "")
        self.table.setRowCount(0)
        for book in books:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(book.book_id)))
            self.table.setItem(row, 1, QTableWidgetItem(book.title))
            self.table.setItem(row, 2, QTableWidgetItem(book.isbn or "N/A"))
            self.table.setItem(row, 3, QTableWidgetItem(book.genre))
            status_item = QTableWidgetItem("Available" if book.isAvailable() else "On Loan")
            status_item.setBackground(QColor("#27ae60") if book.isAvailable() else QColor("#e74c3c"))
            status_item.setForeground(QColor("white"))
            status_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 4, status_item)
            btn = QPushButton("Borrow Now" if book.isAvailable() else "On Loan")
            btn.setEnabled(book.isAvailable())
            btn.clicked.connect(lambda _, bid=book.book_id: self.borrowBook(bid))
            self.table.setCellWidget(row, 5, btn)
        self.table.resizeColumnsToContents()

    def borrowBook(self, bid):
        msg = self.system.borrowBook(bid)
        QMessageBox.information(self, "Borrow Status", msg)
        self.refreshCatalog()
        self.refreshLoans()

    def loansTab(self):
        w = QWidget()
        l = QVBoxLayout(w)
        self.loans_table = QTableWidget()
        self.loans_table.setColumnCount(6)
        self.loans_table.setHorizontalHeaderLabels(
            ["Loan ID", "Book Title", "Borrowed On", "Due Date", "Status", "Action"])
        header = self.loans_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        l.addWidget(QLabel("<h2>My Loan History</h2>", alignment=Qt.AlignCenter))
        l.addWidget(self.loans_table)
        self.refreshLoans()
        return w

    def refreshLoans(self):
        loans = self.system.getMyLoans()  # (LoanID, Title, LoanDate, DueDate, is_active)
        self.loans_table.setRowCount(len(loans))
        for i, loan in enumerate(loans):
            loan_id, title, loan_date, due_date, is_active = loan
            self.loans_table.setItem(i, 0, QTableWidgetItem(str(loan_id)))
            self.loans_table.setItem(i, 1, QTableWidgetItem(title))
            self.loans_table.setItem(i, 2, QTableWidgetItem(str(loan_date)))
            self.loans_table.setItem(i, 3, QTableWidgetItem(str(due_date)))
            if is_active:
                status = QTableWidgetItem("Active Loan")
                status.setBackground(QColor("#e67e22"))
                status.setForeground(QColor("white"))
                status.setTextAlignment(Qt.AlignCenter)
                self.loans_table.setItem(i, 4, status)
                return_btn = QPushButton("Return Book")
                return_btn.setObjectName("returnBtn")
                return_btn.clicked.connect(lambda _, lid=loan_id: self.returnBook(lid))
                self.loans_table.setCellWidget(i, 5, return_btn)
            else:
                status = QTableWidgetItem("Returned")
                status.setBackground(QColor("#27ae60"))
                status.setForeground(QColor("white"))
                status.setTextAlignment(Qt.AlignCenter)
                self.loans_table.setItem(i, 4, status)
                done_item = QTableWidgetItem("Returned")
                done_item.setFlags(Qt.ItemIsEnabled)
                self.loans_table.setItem(i, 5, done_item)

    def returnBook(self, loan_id):
        reply = QMessageBox.question(self, "Return Book",
                                     "Confirm return of this book?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            msg = self.system.returnBook(loan_id)
            QMessageBox.information(self, "Success", msg)
            self.refreshLoans()
            self.refreshCatalog()

    def summaryTab(self):
        tb, tm, al = self.system.getStats()
        w = QWidget()
        l = QVBoxLayout(w)
        l.setAlignment(Qt.AlignCenter)
        l.addSpacing(50)
        stats = [("Total Books", str(tb), "#7f6bff"), ("Total Members", str(tm), "#e67e22"),
                 ("Active Loans", str(al), "#e74c3c"), ("Book Clubs", "5", "#27ae60")]
        for label, val, color in stats:
            lbl = QLabel(label)
            val_lbl = QLabel(val)
            lbl.setAlignment(Qt.AlignCenter)
            val_lbl.setAlignment(Qt.AlignCenter)
            val_lbl.setStyleSheet(f"color: {color}; font-size: 36px; font-weight: bold;")
            l.addWidget(lbl)
            l.addWidget(val_lbl)
            l.addSpacing(20)
        l.addStretch()
        return w

    def bookClubTab(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setAlignment(Qt.AlignCenter)
        l.addSpacing(60)
        title = QLabel("BOOK CLUB MANAGEMENT")
        title.setFont(QFont("Segoe UI", 32, QFont.Bold))
        title.setStyleSheet("color: #d7c6ff;")
        clubs = ["Python Dev Club – 18 members", "Sci-Fi Readers – 25 members",
                 "Clean Code Society – 15 members", "Dystopian Nights – 22 members",
                 "Classics Book Club – 30 members"]
        l.addWidget(title)
        l.addSpacing(40)
        for club in clubs:
            lbl = QLabel("• " + club)
            lbl.setStyleSheet("font-size: 16px;")
            l.addWidget(lbl, alignment=Qt.AlignCenter)
        l.addStretch()
        return w

    def adminTab(self):
        w = QWidget()
        l = QVBoxLayout(w)
        l.addWidget(QLabel("<h1 style='color:#d7c6ff'>Librarian Administrative Panel</h1>", alignment=Qt.AlignCenter))
        admin_tabs = QTabWidget()
        admin_tabs.addTab(self.make_scrollable(self.adminBooksTab()), "Manage Books")
        admin_tabs.addTab(self.make_scrollable(self.adminMembersTab()), "Manage Members")
        admin_tabs.addTab(self.make_scrollable(self.adminAllLoansTab()), "All Loans")
        l.addWidget(admin_tabs)
        return w

    def adminBooksTab(self):
        w = QWidget()
        layout = QVBoxLayout(w)
        layout.setSpacing(20)
        title = QLabel("MANAGE BOOKS")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 26px; font-weight: bold; color: #7f6bff;")
        layout.addWidget(title)
        form_box = QGroupBox("Add New Book")
        form = QFormLayout(form_box)
        form.setLabelAlignment(Qt.AlignRight)
        self.book_title = QLineEdit()
        self.book_isbn = QLineEdit()
        self.book_genre = QComboBox()
        self.book_genre.addItems(["Technical", "Sci-Fi", "Classic", "Dystopian"])
        add_btn = QPushButton("Add Book to Library")
        add_btn.setObjectName("primary")
        add_btn.clicked.connect(self.addNewBook)
        form.addRow("Title:", self.book_title)
        form.addRow("ISBN:", self.book_isbn)
        form.addRow("Genre:", self.book_genre)
        form.addRow("", add_btn)
        layout.addWidget(form_box)
        self.books_table = QTableWidget()
        self.books_table.setColumnCount(5)
        self.books_table.setHorizontalHeaderLabels(["ID", "Title", "ISBN", "Genre", "Action"])
        self.books_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.books_table.verticalHeader().setDefaultSectionSize(50)
        self.loadAdminBooks()
        layout.addWidget(QLabel("All Books in Library"))
        layout.addWidget(self.books_table)
        self.books_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.books_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.books_table.setMinimumHeight(400)
        layout.addWidget(self.books_table, stretch=1)
        return w

    def loadAdminBooks(self):
        books = self.system.searchBooks("")
        self.books_table.setRowCount(len(books))
        for i, b in enumerate(books):
            self.books_table.setItem(i, 0, QTableWidgetItem(str(b.book_id)))
            self.books_table.setItem(i, 1, QTableWidgetItem(b.title))
            self.books_table.setItem(i, 2, QTableWidgetItem(b.isbn or "N/A"))
            self.books_table.setItem(i, 3, QTableWidgetItem(b.genre))
            del_btn = QPushButton("Delete")
            del_btn.setObjectName("red")
            del_btn.clicked.connect(lambda _, bid=b.book_id: self.deleteBook(bid))
            self.books_table.setCellWidget(i, 4, del_btn)

    def addNewBook(self):
        title = self.book_title.text().strip()
        isbn = self.book_isbn.text().strip()
        genre = self.book_genre.currentText()
        if title and isbn:
            self.system.db.add_book(title, isbn, genre)
            QMessageBox.information(self, "Success", f"Book '{title}' added!")
            self.book_title.clear()
            self.book_isbn.clear()
            self.loadAdminBooks()
            self.refreshCatalog()

    def deleteBook(self, book_id):
        if QMessageBox.question(self, "Confirm", "Delete this book?") == QMessageBox.Yes:
            self.system.db.delete_book(book_id)
            QMessageBox.information(self, "Deleted", "Book removed.")
            self.loadAdminBooks()
            self.refreshCatalog()

    def deleteMember(self, member_id):
        # Prevent deletion of the currently logged-in user
        if self.system.loggedInUser and member_id == self.system.loggedInUser.user_id:
            QMessageBox.warning(self, "Action Denied", "You cannot delete your own account while logged in.")
            return

        reply = QMessageBox.question(self, "Confirm Deletion",
                                     f"Are you sure you want to delete the member with ID {member_id}? This cannot be undone.",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                self.system.delete_member(member_id)
                QMessageBox.information(self, "Deleted", f"Member ID {member_id} removed successfully.")
                self.loadMembers()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete member. Error: {e}")


    def adminMembersTab(self):
        w = QWidget()
        layout = QVBoxLayout(w)
        layout.setSpacing(20)
        form_box = QGroupBox("Register New Member")
        form = QFormLayout(form_box)
        self.mem_fname = QLineEdit()
        self.mem_lname = QLineEdit()
        self.mem_email = QLineEdit()
        self.mem_pass = QLineEdit()
        self.mem_pass.setEchoMode(QLineEdit.Password)
        reg_btn = QPushButton("Register Member")
        reg_btn.clicked.connect(self.registerNewMember)
        form.addRow("First Name:", self.mem_fname)
        form.addRow("Last Name:", self.mem_lname)
        form.addRow("Email:", self.mem_email)
        form.addRow("Password:", self.mem_pass)
        form.addRow("", reg_btn)
        layout.addWidget(form_box)
        label = QLabel("All Registered Members")
        layout.addWidget(label)
        self.members_table = QTableWidget()

        self.members_table.setColumnCount(5)
        self.members_table.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Role", "Action"])

        self.members_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.members_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.members_table.setMinimumHeight(400)
        layout.addWidget(self.members_table, stretch=1)
        self.loadMembers()
        return w

    def loadMembers(self):
        members = self.system.db.get_all_members()
        self.members_table.setRowCount(len(members))
        for i, m in enumerate(members):
            member_id = m[0]

            self.members_table.setItem(i, 0, QTableWidgetItem(str(member_id)))
            self.members_table.setItem(i, 1, QTableWidgetItem(f"{m[1]} {m[2]}"))
            self.members_table.setItem(i, 2, QTableWidgetItem(m[3]))
            self.members_table.setItem(i, 3, QTableWidgetItem(m[4]))

            del_btn = QPushButton("Delete")
            del_btn.setObjectName("red")

            del_btn.clicked.connect(lambda _, mid=member_id: self.deleteMember(mid))

            # UX: Disable deletion for the currently logged-in user or other Librarians
            is_self = self.system.loggedInUser and member_id == self.system.loggedInUser.user_id
            is_librarian = m[4] == 'Librarian'

            if is_self or is_librarian:
                del_btn.setEnabled(False)
                del_btn.setText("Librarian" if is_librarian else "Self")

            self.members_table.setCellWidget(i, 4, del_btn)

    def registerNewMember(self):
        fname = self.mem_fname.text().strip()
        lname = self.mem_lname.text().strip()
        email = self.mem_email.text().strip()
        pwd = self.mem_pass.text()
        if all([fname, lname, email, pwd]):
            hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
            self.system.db.create_user(fname, lname, email, 'Member', hashed)
            QMessageBox.information(self, "Success", "Member registered!")
            for f in [self.mem_fname, self.mem_lname, self.mem_email, self.mem_pass]:
                f.clear()
            self.loadMembers()

    def adminAllLoansTab(self):
        w = QWidget()
        layout = QVBoxLayout(w)
        title = QLabel("ALL ACTIVE & HISTORICAL LOANS")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #7f6bff;")
        layout.addWidget(title)
        self.all_loans_table = QTableWidget()
        self.all_loans_table.setColumnCount(7)
        self.all_loans_table.setHorizontalHeaderLabels([
            "Loan ID", "Member", "Book Title", "Borrowed", "Due", "Returned", "Status"
        ])
        self.all_loans_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.loadAllLoans()
        layout.addWidget(self.all_loans_table)
        return w

    def loadAllLoans(self):
        conn = self.system.db.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT l.LoanID, m.FirstName || ' ' || m.LastName, b.Title,
                   l.LoanDate, l.DueDate, l.ReturnDate,
                   CASE WHEN l.ReturnDate IS NULL THEN 'Active' ELSE 'Returned' END
            FROM LOANS l JOIN MEMBERS m ON l.MemberID = m.MemberID
            JOIN BOOKS b ON l.BookID = b.BookID
            ORDER BY l.LoanDate DESC
        """)
        loans = cur.fetchall()
        cur.close()
        conn.close()
        self.all_loans_table.setRowCount(len(loans))
        for i, loan in enumerate(loans):
            for j in range(7):
                item = QTableWidgetItem(str(loan[j]) if loan[j] else "—")
                if j == 6:
                    item.setBackground(QColor("#27ae60") if loan[5] else QColor("#e67e22"))
                    item.setForeground(QColor("white"))
                    item.setTextAlignment(Qt.AlignCenter)
                self.all_loans_table.setItem(i, j, item)