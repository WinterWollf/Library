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
('Elżbieta', 'Kamińska', '567890123456', 'elzbieta.kaminska@example.com', 1),
('Karolina', 'Zalewska', '678901234567', 'karolina.zalewska@example.com', 2),
('Marek', 'Kowalczyk', '789012345678', 'marek.kowalczyk@example.com', 1),
('Anna', 'Lewicka', '890123456789', 'anna.lewicka@example.com', 3),
('Jakub', 'Majewski', '901234567890', 'jakub.majewski@example.com', 2),
('Monika', 'Kozioł', '012345678901', 'monika.koziol@example.com', 1),
('Paweł', 'Nowak', '123450987654', 'pawel.nowak@example.com', 3),
('Dorota', 'Wiśniewska', '234560987654', 'dorota.wisniewska@example.com', 1),
('Jacek', 'Wróbel', '345670987654', 'jacek.wrobel@example.com', 2),
('Magdalena', 'Jankowska', '456780987654', 'magdalena.jankowska@example.com', 3),
('Rafał', 'Kaczmarek', '567890987654', 'rafal.kaczmarek@example.com', 2);

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
('Joanna', 'Kozłowska', 'ul. Wiosenna 3, 10-010 Rzeszów', '012345678901', 'joanna.kozlowska@example.com'),
('Ewa', 'Jankowska', 'ul. Lipowa 4, 11-011 Lublin', '123456789013', 'ewa.jankowska@example.com'),
('Grzegorz', 'Król', NULL, '234567890124', 'grzegorz.krol@example.com'),
('Beata', 'Kaczmarek', 'ul. Długa 6, 12-012 Kraków', '345678901235', 'beata.kaczmarek@example.com'),
('Dawid', 'Maj', 'ul. Leśna 7, 13-013 Katowice', '456789012356', 'dawid.maj@example.com'),
('Natalia', 'Szulc', 'ul. Jasna 8, 14-014 Wrocław', '567890123467', 'natalia.szulc@example.com'),
('Karol', 'Adamski', NULL, '678901234578', 'karol.adamski@example.com'),
('Marta', 'Zając', 'ul. Cicha 9, 15-015 Bydgoszcz', '789012345689', 'marta.zajac@example.com'),
('Wojciech', 'Bąk', 'ul. Szkolna 10, 16-016 Gdynia', '890123456790', 'wojciech.bak@example.com'),
('Julia', 'Lis', 'ul. Wesoła 11, 17-017 Toruń', '901234567801', 'julia.lis@example.com'),
('Patryk', 'Kowalczyk', 'ul. Szeroka 12, 18-018 Olsztyn', '012345678912', 'patryk.kowalczyk@example.com');

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
('joanna_kozlowska', 'haslo123', NULL, 10),
('ewa_jankowska', 'haslo123', NULL, 11),
('grzegorz_krol', 'haslo123', NULL, 12),
('beata_kaczmarek', 'haslo123', NULL, 13),
('dawid_maj', 'haslo123', NULL, 14),
('natalia_szulc', 'haslo123', NULL, 15),
('karol_adamski', 'haslo123', NULL, 16),
('marta_zajac', 'haslo123', NULL, 17),
('wojciech_bak', 'haslo123', NULL, 18),
('julia_lis', 'haslo123', NULL, 19),
('patryk_kowalczyk', 'haslo123', NULL, 20),
('alicja_kwiatkowska', 'alicja_pass', 1, NULL),
('bartosz_nowicki', 'bartek123', 2, NULL),
('wiktor_szyszka', 'test1234', 3, NULL),
('damian_wojcik', 'damian123', 4, NULL),
('elzbieta_kaminska', 'elzbieta987', 5, NULL),
('karolina_zalewska', 'karolina123', 6, NULL),
('marek_kowalczyk', 'marek123', 7, NULL),
('anna_lewicka', 'anna_pass', 8, NULL),
('jakub_majewski', 'jakub123', 9, NULL),
('monika_koziol', 'monika123', 10, NULL),
('pawel_nowak', 'pawel123', 11, NULL),
('dorota_wisniewska', 'dorota123', 12, NULL),
('jacek_wrobel', 'jacek123', 13, NULL),
('magdalena_jankowska', 'magda123', 14, NULL),
('rafal_kaczmarek', 'rafal123', 15, NULL);

CREATE TABLE BookGenres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50) NOT NULL
);

INSERT INTO BookGenres (genre_name) VALUES
(''),
('Fikcja'),
('Literatura faktu'),
('Science Fiction'),
('Fantasy'),
('Kryminał'),
('Thriller'),
('Romans'),
('Horror'),
('Biografia'),
('Historia'),
('Dramat'),
('Poezja'),
('Esej'),
('Komedia'),
('Dystopia'),
('Literatura podróżnicza'),
('Literatura dziecięca'),
('Literatura młodzieżowa'),
('Literatura obyczajowa'),
('Bajka');

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
('George Orwell', '1984', '1949-06-08', 'Secker & Warburg', 15, 19.99),
('Yuval Noah Harari', 'Sapiens', '2011-02-04', NULL, 2, 25.99),
('Isaac Asimov', 'Fundacja', '1951-05-01', 'Gnome Press', 3, 18.50),
('J.R.R. Tolkien', 'Hobbit', '1937-09-21', 'George Allen & Unwin', 4, 22.00),
('Agatha Christie', 'Morderstwo', '1934-01-01', 'Collins Crime Club', 5, 14.99),
('Gillian Flynn', 'Zaginiona dziewczyna', '2012-06-05', NULL, 6, 15.99),
('Jane Austen', 'Duma i uprzedzenie', '1813-01-28', 'T. Egerton', 7, 12.99),
('Stephen King', 'Lśnienie', '1977-01-28', NULL, 8, 20.99),
('Walter Isaacson', 'Steve Jobs', '2011-10-24', 'Simon & Schuster', 9, 29.99),
('Doris Kearns', 'Geniusz polityczny', '2005-10-25', 'Simon & Schuster', 10, 24.99),
('Gabriel Garcia', 'Sto lat samotności', '1967-05-30', 'Harper & Row', 1, 18.99),
('Michelle Obama', 'Becoming', '2018-11-13', 'Crown', 9, 26.99),
('Haruki Murakami', 'Norwegian Wood', '1987-08-04', 'Kodansha', 1, 16.50),
('Stephen Hawking', 'Krótka historia czasu', '1988-04-01', 'Bantam Books', 2, 21.50),
('Terry Pratchett', 'Straż! Straż!', '1989-08-01', 'Gollancz', 4, 17.99),
('Lee Child', 'Poziom śmierci', '1997-03-17', 'Putnam', 6, 13.99),
('Emily Brontë', 'Wichrowe Wzgórza', '1847-12-19', 'Thomas Cautley Newby', 7, 11.50),
('Dean Koontz', 'Straznicy', '1987-01-01', 'Putnam', 8, 19.99),
('Malcolm Gladwell', 'Poza schematem', '2008-11-18', 'Brown and Company', 2, 14.99),
('Dan Brown', 'Kod Leonarda da Vinci', '2003-03-18', 'Doubleday', 5, 23.99),
('Ernest Hemingway', 'Stary człowiek i morze', '1952-09-01', 'Charles Scribners', 1, 15.50),
('Margaret Atwood', 'Opowieść podręcznej', '1985-06-14', 'McClelland & Stewart', 3, 20.99),
('Kazuo Ishiguro', 'Nie opuszczaj mnie', '2005-03-03', 'Faber & Faber', 1, 19.99),
('Jane Austen', 'Emma', '1815-12-23', 'John Murray', 7, 12.50),
('John Grisham', 'Firma', '1991-03-01', 'Doubleday', 6, 18.99),
('Octavia E. Butler', 'Przypływ', '1979-06-01', 'Doubleday', 3, 16.99),
('Ray Bradbury', 'Fahrenheit 451', '1953-10-19', 'Ballantine Books', 3, 14.50),
('George R.R. Martin', 'Gra o tron', '1996-08-06', 'Bantam Spectra', 4, 24.99),
('Khaled Hosseini', 'Chłopiec z latawcem', '2003-05-29', 'Riverhead Books', 1, 16.50),
('Margaret Mitchell', 'Przeminęło z wiatrem', '1936-06-30', 'Macmillan Publishers', 7, 21.99),
('Olga Tokarczuk', 'Bieguni', '2007-09-15', 'Wydawnictwo Literackie', 1, 22.99),
('Stanisław Lem', 'Solaris', '1961-06-20', 'Iskry', 3, 18.99),
('Zofia Nałkowska', 'Granica', '1935-03-18', 'Książnica-Atlas', 7, 15.50),
('Henryk Sienkiewicz', 'Quo Vadis', '1896-03-26', 'Gebethner i Wolff', 10, 19.99),
('Bolesław Prus', 'Lalka', '1890-01-29', 'Gebethner i Wolff', 1, 21.50),
('Adam Mickiewicz', 'Pan Tadeusz', '1834-06-28', 'J.K. Żupańskiego', 7, 14.50),
('Juliusz Słowacki', 'Kordian', '1834-10-31', 'Laskauer', 12, 13.50),
('Witold Gombrowicz', 'Ferdydurke', '1937-12-15', 'Towarzystwo Wydawnicze Rój', 1, 20.50),
('Ryszard Kapuściński', 'Imperium', '1993-11-10', 'Czytelnik', 2, 18.50);

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
(5, 4, '2024-05-23', '2024-08-23', 5),
(1, 6, '2024-05-25', '2024-06-25', 6),
(7, 7, '2024-05-27', '2024-06-27', 7),
(8, 8, '2024-05-29', '2024-06-29', 8),
(9, 9, '2024-05-31', '2024-06-30', 9),
(10, 10, '2024-06-02', '2024-07-02', 10),
(11, 11, '2024-06-04', '2024-07-04', 11),
(12, 12, '2024-06-06', '2024-07-06', 12),
(13, 13, '2024-06-08', '2024-07-08', 13),
(14, 14, '2024-06-10', '2024-07-10', 14),
(15, 15, '2024-06-12', '2024-07-12', 15);

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
(3, 1, '2024-05-29', '2024-06-02', 3, 0),
(4, 3, '2024-05-30', '2024-06-03', 4, 1),
(5, 4, '2024-06-01', '2024-06-05', 5, 0),
(6, 2, '2024-06-03', '2024-06-07', 6, 1),
(7, 5, '2024-06-05', '2024-06-09', 7, 0),
(8, 6, '2024-06-07', '2024-06-11', 8, 1),
(9, 7, '2024-06-09', '2024-06-13', 9, 0),
(10, 8, '2024-06-11', '2024-06-15', 10, 1),
(11, 9, '2024-06-13', '2024-06-17', 11, 0),
(12, 10, '2024-06-15', '2024-06-19', 12, 1),
(13, 11, '2024-06-17', '2024-06-21', 13, 0),
(14, 12, '2024-06-19', '2024-06-23', 14, 1),
(15, 13, '2024-06-21', '2024-06-25', 15, 0);

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
