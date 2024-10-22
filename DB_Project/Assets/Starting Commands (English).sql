CREATE TABLE Librarians (
    librarian_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    phone_number CHAR(12) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    security_level TINYINT NOT NULL CHECK (security_level BETWEEN 1 AND 3)
);

INSERT INTO Librarians (name, surname, phone_number, email, security_level) VALUES
('Alicja', 'Kwiatkowska', '123456789012', 'alicja.kwiatkowska@example.com', 1),
('Bartosz', 'Nowicki', '234567890123', 'bartosz.nowicki@example.com', 2),
('Wiktor', 'Szyszka', '345678901234', 'wiktor.szyszka@example.com', 3),
('Damian', 'Wójcik', '456789012345', 'damian.wojcik@example.com', 2),
('Elżbieta', 'Kamińska', '567890123456', 'elzbieta.kaminska@example.com', 1);

CREATE TABLE Readers (
    reader_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    phone_number VARCHAR(12) NOT NULL,
    email VARCHAR(100) UNIQUE
);

INSERT INTO Readers (name, surname, address, phone_number, email) VALUES
('Jan', 'Kowalski', 'ul. Kwiatowa 15, 00-001 Warszawa', '123456789012', 'jan.kowalski@example.com'),
('Anna', 'Nowak', NULL, '234567890123', 'anna.nowak@example.com'),
('Piotr', 'Wiśniewski', 'ul. Słoneczna 10, 03-003 Gdańsk', '345678901234', 'piotr.wisniewski@example.com'),
('Katarzyna', 'Wójcik', 'ul. Morska 8, 04-004 Poznań', '456789012345', 'katarzyna.wojcik@example.com'),
('Tomasz', 'Kamiński', NULL, '567890123456', 'tomasz.kaminski@example.com'),
('Maria', 'Lewandowska', 'ul. Zielona 25, 06-006 Łódź', '678901234567', 'maria.lewandowska@example.com'),
('Michał', 'Zieliński', NULL, '789012345678', 'michal.zielinski@example.com'),
('Agnieszka', 'Szymańska', 'ul. Wiejska 12, 08-008 Białystok', '890123456789', 'agnieszka.szymanska@example.com'),
('Robert', 'Woźniak', NULL, '901234567890', 'robert.wozniak@example.com'),
('Joanna', 'Kozłowska', 'ul. Wiosenna 3, 10-010 Rzeszów', '012345678901', 'joanna.kozlowska@example.com');

CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    librarian_id INT UNIQUE,
    reader_id INT UNIQUE,
    FOREIGN KEY (librarian_id) REFERENCES Librarians(librarian_id) ON DELETE CASCADE,
    FOREIGN KEY (reader_id) REFERENCES Readers(reader_id) ON DELETE CASCADE
);

-- Dodawanie nowych użytkowników, którzy są czytelnikami
INSERT INTO Users (username, password, librarian_id, reader_id) VALUES
('jan_kowalski', 'haslo123', NULL, 1),
('anna_nowak', 'anna123', NULL, 2),
('piotr_wisniewski', 'p1otr12', NULL, 3),
('katarzyna_wojcik', 'kw123', NULL, 4),
('tomasz_kaminski', 'tomasz789', NULL, 5),
('maria_lewandowska', 'haslo123', NULL, 6),
('michal_zielinski', 'haslo123', NULL, 7),
('agnieszka_szymanska', 'haslo123', NULL, 8),
('robert_wozniak', 'haslo123', NULL, 9),
('joanna_kozlowska', 'haslo123', NULL, 10);

-- Dodawanie nowych użytkowników, którzy są bibliotekarzami
INSERT INTO Users (username, password, librarian_id, reader_id) VALUES
('alicja_kwiatkowska', 'alicja_pass', 1, NULL),
('bartosz_nowicki', 'bartek123', 2, NULL),
('wiktor_szyszka', 'test1234', 3, NULL),
('damian_wojcik', 'damian123', 4, NULL),
('elzbieta_kaminska', 'elzbieta987', 5, NULL);

CREATE TABLE BookGenres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50) NOT NULL
);

INSERT INTO BookGenres (genre_name) VALUES
(''),
('Fiction'),
('Non-Fiction'),
('Science Fiction'),
('Fantasy'),
('Mystery'),
('Thriller'),
('Romance'),
('Horror'),
('Biography'),
('History');

CREATE TABLE Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    author VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    release_date DATE NOT NULL,
    publishing_house VARCHAR(100),
    book_genre_id INT,
    price DECIMAL(6, 2) NOT NULL,
    FOREIGN KEY (book_genre_id) REFERENCES BookGenres(genre_id)
);

INSERT INTO Books (author, title, release_date, publishing_house, book_genre_id, price) VALUES
('George Orwell', '1984', '1949-06-08', 'Secker & Warburg', 2, 19.99),
('Yuval Noah Harari', 'Sapiens: A Brief History of Humankind', '2011-02-04', NULL, 3, 25.99),
('Isaac Asimov', 'Foundation', '1951-05-01', 'Gnome Press', 4, 18.50),
('J.R.R. Tolkien', 'The Hobbit', '1937-09-21', 'George Allen & Unwin', 5, 22.00),
('Agatha Christie', 'Murder on the Orient Express', '1934-01-01', 'Collins Crime Club', 6, 14.99),
('Gillian Flynn', 'Gone Girl', '2012-06-05', NULL, 7, 15.99),
('Jane Austen', 'Pride and Prejudice', '1813-01-28', 'T. Egerton', 8, 12.99),
('Stephen King', 'The Shining', '1977-01-28', NULL, 9, 20.99),
('Walter Isaacson', 'Steve Jobs', '2011-10-24', 'Simon & Schuster', 10, 29.99),
('Doris Kearns Goodwin', 'Team of Rivals: The Political Genius of Abraham Lincoln', '2005-10-25', 'Simon & Schuster', 11, 24.99),
('J.R.R. Tolkien', 'The Hobbit 2', '1937-09-21', 'George Allen & Unwin', 5, 22.00);

CREATE TABLE BookRentals (
    rental_id INT PRIMARY KEY AUTO_INCREMENT,
    reader_id INT,
    book_id INT,
    rental_date DATE,
    potential_return_date DATE,
    librarian_id INT,
    FOREIGN KEY (reader_id) REFERENCES Readers(reader_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (librarian_id) REFERENCES Librarians(librarian_id)
);

INSERT INTO BookRentals (reader_id, book_id, rental_date, potential_return_date, librarian_id) VALUES
(1, 1, '2024-05-15', '2024-05-27', 1),
(2, 3, '2024-05-17', '2024-05-20', 2),
(3, 2, '2024-05-19', '2024-06-19', 3),
(4, 5, '2024-05-21', '2024-05-29', 4),
(5, 4, '2024-05-23', '2024-08-23', 5);

CREATE TABLE History (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    date_of_return DATE,
    potential_return_date DATE,
    librarian_id INT,
    belated BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (librarian_id) REFERENCES Librarians(librarian_id)
);

INSERT INTO History (user_id, book_id, date_of_return, potential_return_date, librarian_id, belated) VALUES
(1, 1, '2024-05-25', '2024-05-29', 1, 0),
(2, 1, '2024-05-27', '2024-06-01', 2, 1),
(3, 1, '2024-05-29', '2024-06-02', 3, 0);

CREATE TABLE BooksCovers (
    cover_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    path VARCHAR(200),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

INSERT INTO BooksCovers (book_id, path) VALUES
(4, 'hobbit.png'),
(7, 'duma.png'),
(9, 'steve.png'),
(12, 'becoming.png'),
(27, 'fahrenheit451.png'),
(28, 'gra.png'),
(29, 'chlopiec.png'),
(31, 'bieguni.png'),
(32, 'solaris.png'),
(33, 'granica.png'),
(35, 'lalka.png'),
(36, 'pantadeusz.png');

-- Dodatkowe pozycje
INSERT INTO Books (author, title, release_date, publishing_house, book_genre_id, price) VALUES
('Gabriel Garcia Marquez', 'One Hundred Years of Solitude', '1967-05-30', 'Harper & Row', 2, 18.99),
('Michelle Obama', 'Becoming', '2018-11-13', 'Crown', 10, 26.99),
('Haruki Murakami', 'Norwegian Wood', '1987-08-04', 'Kodansha', 2, 16.50),
('Stephen Hawking', 'A Brief History of Time', '1988-04-01', 'Bantam Books', 3, 21.50),
('Terry Pratchett', 'Guards! Guards!', '1989-08-01', 'Gollancz', 5, 17.99),
('Lee Child', 'Killing Floor', '1997-03-17', 'Putnam', 7, 13.99),
('Emily Brontë', 'Wuthering Heights', '1847-12-19', 'Thomas Cautley Newby', 8, 11.50),
('Dean Koontz', 'Watchers', '1987-01-01', 'Putnam', 9, 19.99),
('Malcolm Gladwell', 'Outliers: The Story of Success', '2008-11-18', 'Little, Brown and Company', 3, 14.99),
('Dan Brown', 'The Da Vinci Code', '2003-03-18', 'Doubleday', 6, 23.99),
('Ernest Hemingway', 'The Old Man and the Sea', '1952-09-01', 'Charles Scribner\'s Sons', 2, 15.50),
('Margaret Atwood', 'The Handmaid\'s Tale', '1985-06-14', 'McClelland & Stewart', 4, 20.99),
('Kazuo Ishiguro', 'Never Let Me Go', '2005-03-03', 'Faber & Faber', 2, 19.99),
('Jane Austen', 'Emma', '1815-12-23', 'John Murray', 8, 12.50),
('John Grisham', 'The Firm', '1991-03-01', 'Doubleday', 7, 18.99),
('Octavia E. Butler', 'Kindred', '1979-06-01', 'Doubleday', 4, 16.99),
('Ray Bradbury', 'Fahrenheit 451', '1953-10-19', 'Ballantine Books', 4, 14.50),
('George R.R. Martin', 'A Game of Thrones', '1996-08-06', 'Bantam Spectra', 5, 24.99),
('Khaled Hosseini', 'The Kite Runner', '2003-05-29', 'Riverhead Books', 2, 16.50),
('Margaret Mitchell', 'Gone with the Wind', '1936-06-30', 'Macmillan Publishers', 8, 21.99);
