
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

CREATE TABLE AUTHORS (
    AuthorID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);

CREATE TABLE BOOKS (
    BookID SERIAL PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    ISBN VARCHAR(13) UNIQUE,
    PublicationDate DATE,
    Genre VARCHAR(50),
    Status VARCHAR(20) DEFAULT 'Available' CHECK (Status IN ('Available', 'On Loan'))
);

CREATE TABLE BOOKAUTHOR (
    BookID INT REFERENCES BOOKS(BookID),
    AuthorID INT REFERENCES AUTHORS(AuthorID),
    PRIMARY KEY (BookID, AuthorID)
);

CREATE TABLE MEMBERS (
    MemberID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    JoinDate DATE NOT NULL,
    Role VARCHAR(20) CHECK (Role IN ('Member', 'Librarian')) NOT NULL
);

CREATE TABLE AUTHENTICATION (
    MemberID INTEGER PRIMARY KEY REFERENCES MEMBERS(MemberID) ON DELETE CASCADE,
    PasswordHash VARCHAR(255) NOT NULL,
    LastLogin DATE
);

CREATE TABLE BOOKCLUBS (
    ClubID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    MeetingSchedule VARCHAR(100),
    Topic VARCHAR(50)
);

CREATE TABLE CLUBMEMBERSHIP (
    MemberID INT REFERENCES MEMBERS(MemberID),
    ClubID INT REFERENCES BOOKCLUBS(ClubID),
    PRIMARY KEY (MemberID, ClubID)
);

CREATE TABLE LOANS (
    LoanID SERIAL PRIMARY KEY,
    BookID INTEGER REFERENCES BOOKS(BookID) ON DELETE SET NULL,
    MemberID INTEGER REFERENCES MEMBERS(MemberID) ON DELETE SET NULL,
    LoanDate DATE NOT NULL DEFAULT CURRENT_DATE,
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    Status VARCHAR(20) DEFAULT 'On Loan'
);


INSERT INTO MEMBERS (FirstName, LastName, Email, JoinDate, Role) VALUES
('Abdulai', 'Bah', 'abdulai@gmail.com', '2025-01-01', 'Librarian'),
('Josephine', 'Conteh', 'josephine@gmail.com', '2025-01-02', 'Member'),
('Rilwan', 'Jalloh', 'rilwan@gmail.com', '2025-01-15', 'Member'),
('Emma', 'Wilson', 'emma.w@library.com', '2025-02-10', 'Member'),
('Liam', 'Brown', 'liam.brown@uni.com', '2025-02-20', 'Member'),
('Olivia', 'Taylor', 'olivia.t@uni.com', '2025-03-05', 'Member'),
('Noah', 'Davis', 'noah.davis@uni.com', '2025-03-15', 'Member'),
('Ava', 'Miller', 'ava.miller@library.com', '2025-04-01', 'Librarian'),
('Sophia', 'Garcia', 'sophia.g@uni.com', '2025-04-10', 'Member'),
('Mason', 'Jones', 'mason.jones@uni.com', '2025-05-01', 'Member');


INSERT INTO AUTHENTICATION (MemberID, PasswordHash, LastLogin) VALUES
(1, '$2b$12$5S21at4bTuFBy0H5z6r2A.XZPz4Vp8IrxMtgAuEUX74pW7TZ2a8c6', CURRENT_DATE),
(2, '$2b$12$yg8Cr6xCywO9zHXPiVH6reEz.yAKLbLSAW7tXVP/eE263s.JqePKa', CURRENT_DATE),
(3, '$2b$12$PlaceholderHashJohn0000000000000000000000000000000000000000000', NULL),
(4, '$2b$12$PlaceholderHashEmma0000000000000000000000000000000000000000000', NULL),
(5, '$2b$12$PlaceholderHashLiam0000000000000000000000000000000000000000000', NULL),
(6, '$2b$12$PlaceholderHashOlivia000000000000000000000000000000000000000', NULL),
(7, '$2b$12$PlaceholderHashNoah0000000000000000000000000000000000000000', NULL),
(8, '$2b$12$PlaceholderHashAva00000000000000000000000000000000000000000', NULL),
(9, '$2b$12$PlaceholderHashSophia000000000000000000000000000000000000000', NULL),
(10,'$2b$12$PlaceholderHashMason0000000000000000000000000000000000000000', NULL);


INSERT INTO BOOKS (Title, ISBN, PublicationDate, Genre, Status) VALUES
('The Martian', '9780553418029', '2014-02-11', 'Sci-Fi', 'Available'),
('Python Crash Course', '9781718502703', '2023-01-10', 'Technical', 'Available'),
('Pride and Prejudice', '9780141439518', '1813-01-28', 'Classic', 'Available'),
('Dune', '9780441013593', '1965-08-01', 'Sci-Fi', 'Available'),
('Clean Code', '9780132350884', '2008-08-01', 'Technical', 'Available'),
('1984', '9780451524935', '1949-06-08', 'Dystopian', 'Available'),
('To Kill a Mockingbird', '9780061120084', '1960-07-11', 'Classic', 'Available'),
('The Hobbit', '9780547928227', '1937-09-21', 'Fantasy', 'Available'),
('Sapiens', '9780062316097', '2015-02-10', 'Non-fiction', 'Available'),
('Atomic Habits', '9780735211292', '2018-10-16', 'Self-help', 'Available');


INSERT INTO AUTHORS (FirstName, LastName, BirthDate) VALUES
('Andy', 'Weir', '1972-06-16'),
('Eric', 'Matthes', '1980-01-01'),
('Jane', 'Austen', '1775-12-16'),
('Frank', 'Herbert', '1920-10-08'),
('Robert', 'Martin', '1952-12-05'),
('George', 'Orwell', '1903-06-25'),
('Harper', 'Lee', '1926-04-28'),
('J.R.R.', 'Tolkien', '1892-01-03'),
('Yuval Noah', 'Harari', '1976-02-24'),
('James', 'Clear', '1986-01-16');

INSERT INTO BOOKAUTHOR (BookID, AuthorID) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10);


INSERT INTO BOOKCLUBS (Name, MeetingSchedule, Topic) VALUES
('Sci-Fi Explorers', 'Weekly Fridays', 'Sci-Fi'),
('Tech Book Club', 'Bi-weekly Mondays', 'Technical'),
('Classics Corner', 'Monthly 1st Tuesday', 'Classic'),
('Fantasy Realm', 'Weekly Wednesdays', 'Fantasy'),
('Non-Fiction Nerds', 'Bi-weekly Thursdays', 'Non-fiction'),
('Mystery & Thriller', 'Monthly 3rd Monday', 'Mystery'),
('History Buffs', 'Monthly 2nd Saturday', 'History'),
('Philosophy Circle', 'Bi-weekly Sundays', 'Philosophy'),
('Poetry Lovers', 'Monthly last Friday', 'Poetry'),
('Young Adult Reads', 'Weekly Tuesdays', 'Young Adult');


INSERT INTO CLUBMEMBERSHIP (MemberID, ClubID) VALUES
(1,1),(2,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,7),(9,8),(10,9);


INSERT INTO LOANS (BookID, MemberID, LoanDate, DueDate, ReturnDate, Status) VALUES
(1, 2, '2025-11-01', '2025-11-15', '2025-11-10', 'Returned'),
(2, 3, '2025-11-05', '2025-11-19', NULL, 'On Loan'),
(3, 4, '2025-11-10', '2025-11-24', NULL, 'On Loan'),
(4, 5, '2025-11-12', '2025-11-26', '2025-11-20', 'Returned'),
(5, 6, '2025-11-15', '2025-11-29', NULL, 'On Loan'),
(6, 7, '2025-11-18', '2025-12-02', NULL, 'On Loan'),
(7, 8, '2025-11-20', '2025-12-04', NULL, 'On Loan'),
(8, 9, '2025-11-22', '2025-12-06', '2025-11-28', 'Returned'),
(9, 10, '2025-11-25', '2025-12-09', NULL, 'On Loan'),
(10, 2, '2025-11-28', '2025-12-12', NULL, 'On Loan');



-- Retrieve all books and their availability
SELECT 
    b.BookID,
    b.Title,
    b.Genre,
    CASE 
        WHEN l.Status = 'On Loan' THEN 'On Loan'
        ELSE 'Available'
    END AS Availability
FROM BOOKS b
LEFT JOIN LOANS l 
    ON b.BookID = l.BookID 
    AND l.Status = 'On Loan';

-- Find books by a specific author
SELECT 
    b.BookID,
    b.Title,
    a.FirstName || ' ' || a.LastName AS Author
FROM BOOKS b
JOIN BOOKAUTHOR ba ON b.BookID = ba.BookID
JOIN AUTHORS a ON ba.AuthorID = a.AuthorID
WHERE a.LastName = 'Martin';   -- Example filter


-- List members in a specific book club
SELECT 
    m.MemberID,
    m.FirstName,
    m.LastName,
    bc.Name AS ClubName
FROM MEMBERS m
JOIN CLUBMEMBERSHIP cm ON m.MemberID = cm.MemberID
JOIN BOOKCLUBS bc ON cm.ClubID = bc.ClubID
WHERE bc.Name = 'Tech Book Club';   -- Example club


-- Track currently borrowed books and due dates
SELECT 
    l.LoanID,
    b.Title,
    m.FirstName || ' ' || m.LastName AS Borrower,
    l.LoanDate,
    l.DueDate,
    l.Status
FROM LOANS l
JOIN BOOKS b ON l.BookID = b.BookID
JOIN MEMBERS m ON l.MemberID = m.MemberID
WHERE l.Status = 'On Loan';

-- Create FUNCTIONS (e.g., check overdue books)
CREATE OR REPLACE FUNCTION get_overdue_books()
RETURNS TABLE (
    LoanID INT,
    BookTitle VARCHAR,
    MemberName VARCHAR,
    DueDate DATE
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        l.LoanID,
        b.Title,
        m.FirstName || ' ' || m.LastName AS MemberName,
        l.DueDate
    FROM LOANS l
    JOIN BOOKS b ON l.BookID = b.BookID
    JOIN MEMBERS m ON l.MemberID = m.MemberID
    WHERE l.ReturnDate IS NULL
      AND l.DueDate < CURRENT_DATE;
END;
$$ LANGUAGE plpgsql;


-- Trigger: When a loan is created → Book becomes 'On Loan'
CREATE OR REPLACE FUNCTION set_book_on_loan()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE BOOKS 
    SET Status = 'On Loan'
    WHERE BookID = NEW.BookID;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_book_on_loan
AFTER INSERT ON LOANS
FOR EACH ROW
WHEN (NEW.Status = 'On Loan')
EXECUTE FUNCTION set_book_on_loan();

-- Trigger: When a loan is updated with a return date → Book becomes 'Available'
CREATE OR REPLACE FUNCTION set_book_available()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.ReturnDate IS NOT NULL THEN
        UPDATE BOOKS 
        SET Status = 'Available'
        WHERE BookID = NEW.BookID;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_book_returned
AFTER UPDATE ON LOANS
FOR EACH ROW
WHEN (NEW.ReturnDate IS NOT NULL)
EXECUTE FUNCTION set_book_available();


-- Write JOINS to combine data from multiple tables
SELECT 
    b.BookID,
    b.Title,
    a.FirstName || ' ' || a.LastName AS Author
FROM BOOKS b
JOIN BOOKAUTHOR ba ON b.BookID = ba.BookID
JOIN AUTHORS a ON ba.AuthorID = a.AuthorID;

-- Books and the members who borrowed them
SELECT 
    b.Title,
    m.FirstName || ' ' || m.LastName AS Borrower,
    l.LoanDate,
    l.DueDate,
    l.Status
FROM LOANS l
JOIN BOOKS b ON l.BookID = b.BookID
JOIN MEMBERS m ON l.MemberID = m.MemberID;

-- View: Books currently borrowed by members
CREATE OR REPLACE VIEW vw_current_loans AS
SELECT 
    l.LoanID,
    b.Title,
    m.FirstName || ' ' || m.LastName AS Borrower,
    l.LoanDate,
    l.DueDate
FROM LOANS l
JOIN BOOKS b ON l.BookID = b.BookID
JOIN MEMBERS m ON l.MemberID = m.MemberID
WHERE l.Status = 'On Loan';

-- Run it
SELECT * FROM vw_current_loans;

-- View: Books with authors 
CREATE OR REPLACE VIEW vw_books_with_authors AS
SELECT 
    b.BookID,
    b.Title,
    STRING_AGG(a.FirstName || ' ' || a.LastName, ', ') AS Authors,
    b.Status
FROM BOOKS b
JOIN BOOKAUTHOR ba ON b.BookID = ba.BookID
JOIN AUTHORS a ON ba.AuthorID = a.AuthorID
GROUP BY b.BookID, b.Title, b.Status;

-- View: Overdue books
CREATE OR REPLACE VIEW vw_overdue_books AS
SELECT 
    l.LoanID,
    b.Title,
    m.FirstName || ' ' || m.LastName AS Member,
    l.DueDate
FROM LOANS l
JOIN BOOKS b ON l.BookID = b.BookID
JOIN MEMBERS m ON l.MemberID = m.MemberID
WHERE l.ReturnDate IS NULL
  AND l.DueDate < CURRENT_DATE;


