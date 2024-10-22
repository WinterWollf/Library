-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookgenres`
--

DROP TABLE IF EXISTS `bookgenres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookgenres` (
  `genre_id` int(11) NOT NULL AUTO_INCREMENT,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookgenres`
--

LOCK TABLES `bookgenres` WRITE;
/*!40000 ALTER TABLE `bookgenres` DISABLE KEYS */;
INSERT INTO `bookgenres` VALUES (1,'Fikcja'),(2,'Literatura faktu'),(3,'Science Fiction'),(4,'Fantasy'),(5,'Kryminał'),(6,'Thriller'),(7,'Romans'),(8,'Horror'),(9,'Biografia'),(10,'Historia'),(11,'Dramat'),(12,'Poezja'),(13,'Esej'),(14,'Komedia'),(15,'Dystopia'),(16,'Literatura podróżnicza'),(17,'Literatura dziecięca'),(18,'Literatura młodzieżowa'),(19,'Literatura obyczajowa'),(20,'Bajka');
/*!40000 ALTER TABLE `bookgenres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookrentals`
--

DROP TABLE IF EXISTS `bookrentals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookrentals` (
  `rental_id` int(11) NOT NULL AUTO_INCREMENT,
  `reader_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `rental_date` date DEFAULT NULL,
  `potential_return_date` date DEFAULT NULL,
  `librarian_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`rental_id`),
  KEY `reader_id` (`reader_id`),
  KEY `book_id` (`book_id`),
  KEY `librarian_id` (`librarian_id`),
  CONSTRAINT `bookrentals_ibfk_1` FOREIGN KEY (`reader_id`) REFERENCES `readers` (`reader_id`),
  CONSTRAINT `bookrentals_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`),
  CONSTRAINT `bookrentals_ibfk_3` FOREIGN KEY (`librarian_id`) REFERENCES `librarians` (`librarian_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookrentals`
--

LOCK TABLES `bookrentals` WRITE;
/*!40000 ALTER TABLE `bookrentals` DISABLE KEYS */;
INSERT INTO `bookrentals` VALUES (1,1,1,'2024-05-15','2024-05-27',1),(2,2,3,'2024-05-17','2024-05-20',2),(3,3,2,'2024-05-19','2024-06-19',3),(4,4,5,'2024-05-21','2024-05-29',4),(5,5,4,'2024-05-23','2024-08-23',5),(6,1,6,'2024-05-25','2024-06-25',6),(7,7,7,'2024-05-27','2024-06-27',7),(8,8,8,'2024-05-29','2024-06-29',8),(9,9,9,'2024-05-31','2024-06-30',9),(10,10,10,'2024-06-02','2024-07-02',10),(11,11,11,'2024-06-04','2024-07-04',11),(12,12,12,'2024-06-06','2024-07-06',12),(13,13,13,'2024-06-08','2024-07-08',13),(14,14,14,'2024-06-10','2024-07-10',14),(15,15,15,'2024-06-12','2024-07-12',15);
/*!40000 ALTER TABLE `bookrentals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `release_date` date NOT NULL,
  `publishing_house` varchar(100) DEFAULT NULL,
  `book_genre_id` int(11) DEFAULT NULL,
  `price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`book_id`),
  KEY `book_genre_id` (`book_genre_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`book_genre_id`) REFERENCES `bookgenres` (`genre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'George Orwell','1984','1949-06-08','Secker & Warburg',15,19.99),(2,'Yuval Noah Harari','Sapiens','2011-02-04',NULL,2,25.99),(3,'Isaac Asimov','Fundacja','1951-05-01','Gnome Press',3,18.50),(4,'J.R.R. Tolkien','Hobbit','1937-09-21','George Allen & Unwin',4,22.00),(5,'Agatha Christie','Morderstwo','1934-01-01','Collins Crime Club',5,14.99),(6,'Gillian Flynn','Zaginiona dziewczyna','2012-06-05',NULL,6,15.99),(7,'Jane Austen','Duma i uprzedzenie','1813-01-28','T. Egerton',7,12.99),(8,'Stephen King','Lśnienie','1977-01-28',NULL,8,20.99),(9,'Walter Isaacson','Steve Jobs','2011-10-24','Simon & Schuster',9,29.99),(10,'Doris Kearns','Geniusz polityczny','2005-10-25','Simon & Schuster',10,24.99),(11,'Gabriel Garcia','Sto lat samotności','1967-05-30','Harper & Row',1,18.99),(12,'Michelle Obama','Becoming','2018-11-13','Crown',9,26.99),(13,'Haruki Murakami','Norwegian Wood','1987-08-04','Kodansha',1,16.50),(14,'Stephen Hawking','Krótka historia czasu','1988-04-01','Bantam Books',2,21.50),(15,'Terry Pratchett','Straż! Straż!','1989-08-01','Gollancz',4,17.99),(16,'Lee Child','Poziom śmierci','1997-03-17','Putnam',6,13.99),(17,'Emily Brontë','Wichrowe Wzgórza','1847-12-19','Thomas Cautley Newby',7,11.50),(18,'Dean Koontz','Straznicy','1987-01-01','Putnam',8,19.99),(19,'Malcolm Gladwell','Poza schematem','2008-11-18','Brown and Company',2,14.99),(20,'Dan Brown','Kod Leonarda da Vinci','2003-03-18','Doubleday',5,23.99),(21,'Ernest Hemingway','Stary człowiek i morze','1952-09-01','Charles Scribners',1,15.50),(22,'Margaret Atwood','Opowieść podręcznej','1985-06-14','McClelland & Stewart',3,20.99),(23,'Kazuo Ishiguro','Nie opuszczaj mnie','2005-03-03','Faber & Faber',1,19.99),(24,'Jane Austen','Emma','1815-12-23','John Murray',7,12.50),(25,'John Grisham','Firma','1991-03-01','Doubleday',6,18.99),(26,'Octavia E. Butler','Przypływ','1979-06-01','Doubleday',3,16.99),(27,'Ray Bradbury','Fahrenheit 451','1953-10-19','Ballantine Books',3,14.50),(28,'George R.R. Martin','Gra o tron','1996-08-06','Bantam Spectra',4,24.99),(29,'Khaled Hosseini','Chłopiec z latawcem','2003-05-29','Riverhead Books',1,16.50),(30,'Margaret Mitchell','Przeminęło z wiatrem','1936-06-30','Macmillan Publishers',7,21.99),(31,'Olga Tokarczuk','Bieguni','2007-09-15','Wydawnictwo Literackie',1,22.99),(32,'Stanisław Lem','Solaris','1961-06-20','Iskry',3,18.99),(33,'Zofia Nałkowska','Granica','1935-03-18','Książnica-Atlas',7,15.50),(34,'Henryk Sienkiewicz','Quo Vadis','1896-03-26','Gebethner i Wolff',10,19.99),(35,'Bolesław Prus','Lalka','1890-01-29','Gebethner i Wolff',1,21.50),(36,'Adam Mickiewicz','Pan Tadeusz','1834-06-28','J.K. Żupańskiego',7,14.50),(37,'Juliusz Słowacki','Kordian','1834-10-31','Laskauer',12,13.50),(38,'Witold Gombrowicz','Ferdydurke','1937-12-15','Towarzystwo Wydawnicze Rój',1,20.50),(39,'Ryszard Kapuściński','Imperium','1993-11-10','Czytelnik',2,18.50);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookscovers`
--

DROP TABLE IF EXISTS `bookscovers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookscovers` (
  `cover_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`cover_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `bookscovers_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookscovers`
--

LOCK TABLES `bookscovers` WRITE;
/*!40000 ALTER TABLE `bookscovers` DISABLE KEYS */;
INSERT INTO `bookscovers` VALUES (1,4,'hobbit.png'),(2,7,'duma.png'),(3,9,'steve.png'),(4,12,'becoming.png'),(5,27,'fahrenheit451.png'),(6,28,'gra.png'),(7,29,'chlopiec.png'),(8,31,'bieguni.png'),(9,32,'solaris.png'),(10,33,'granica.png'),(11,35,'lalka.png'),(12,36,'pantadeusz.png');
/*!40000 ALTER TABLE `bookscovers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `history_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `date_of_return` date DEFAULT NULL,
  `potential_return_date` date DEFAULT NULL,
  `librarian_id` int(11) DEFAULT NULL,
  `belated` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `user_id` (`user_id`),
  KEY `book_id` (`book_id`),
  KEY `librarian_id` (`librarian_id`),
  CONSTRAINT `history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `history_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`),
  CONSTRAINT `history_ibfk_3` FOREIGN KEY (`librarian_id`) REFERENCES `librarians` (`librarian_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,1,1,'2024-05-25','2024-05-29',1,0),(2,2,1,'2024-05-27','2024-06-01',2,1),(3,3,1,'2024-05-29','2024-06-02',3,0),(4,4,3,'2024-05-30','2024-06-03',4,1),(5,5,4,'2024-06-01','2024-06-05',5,0),(6,6,2,'2024-06-03','2024-06-07',6,1),(7,7,5,'2024-06-05','2024-06-09',7,0),(8,8,6,'2024-06-07','2024-06-11',8,1),(9,9,7,'2024-06-09','2024-06-13',9,0),(10,10,8,'2024-06-11','2024-06-15',10,1),(11,11,9,'2024-06-13','2024-06-17',11,0),(12,12,10,'2024-06-15','2024-06-19',12,1),(13,13,11,'2024-06-17','2024-06-21',13,0),(14,14,12,'2024-06-19','2024-06-23',14,1),(15,15,13,'2024-06-21','2024-06-25',15,0);
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarians`
--

DROP TABLE IF EXISTS `librarians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `librarians` (
  `librarian_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `phone_number` char(12) NOT NULL,
  `email` varchar(100) NOT NULL,
  `security_level` tinyint(4) NOT NULL CHECK (`security_level` between 1 and 3),
  PRIMARY KEY (`librarian_id`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarians`
--

LOCK TABLES `librarians` WRITE;
/*!40000 ALTER TABLE `librarians` DISABLE KEYS */;
INSERT INTO `librarians` VALUES (1,'Alicja','Kwiatkowska','123456789012','alicja.kwiatkowska@example.com',1),(2,'Bartosz','Nowicki','234567890123','bartosz.nowicki@example.com',2),(3,'Wiktor','Szyszka','345678901234','wiktor.szyszka@example.com',3),(4,'Damian','Wójcik','456789012345','damian.wojcik@example.com',2),(5,'Elżbieta','Kamińska','567890123456','elzbieta.kaminska@example.com',1),(6,'Karolina','Zalewska','678901234567','karolina.zalewska@example.com',2),(7,'Marek','Kowalczyk','789012345678','marek.kowalczyk@example.com',1),(8,'Anna','Lewicka','890123456789','anna.lewicka@example.com',3),(9,'Jakub','Majewski','901234567890','jakub.majewski@example.com',2),(10,'Monika','Kozioł','012345678901','monika.koziol@example.com',1),(11,'Paweł','Nowak','123450987654','pawel.nowak@example.com',3),(12,'Dorota','Wiśniewska','234560987654','dorota.wisniewska@example.com',1),(13,'Jacek','Wróbel','345670987654','jacek.wrobel@example.com',2),(14,'Magdalena','Jankowska','456780987654','magdalena.jankowska@example.com',3),(15,'Rafał','Kaczmarek','567890987654','rafal.kaczmarek@example.com',2);
/*!40000 ALTER TABLE `librarians` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `readers`
--

DROP TABLE IF EXISTS `readers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `readers` (
  `reader_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone_number` varchar(12) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`reader_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `readers`
--

LOCK TABLES `readers` WRITE;
/*!40000 ALTER TABLE `readers` DISABLE KEYS */;
INSERT INTO `readers` VALUES (1,'Jan','Kowalski','ul. Kwiatowa 15, 00-001 Warszawa','123456789012','jan.kowalski@example.com'),(2,'Anna','Nowak',NULL,'234567890123','anna.nowak@example.com'),(3,'Piotr','Wiśniewski','ul. Słoneczna 10, 03-003 Gdańsk','345678901234','piotr.wisniewski@example.com'),(4,'Katarzyna','Wójcik','ul. Morska 8, 04-004 Poznań','456789012345','katarzyna.wojcik@example.com'),(5,'Tomasz','Kamiński',NULL,'567890123456','tomasz.kaminski@example.com'),(6,'Maria','Lewandowska','ul. Zielona 25, 06-006 Łódź','678901234567','maria.lewandowska@example.com'),(7,'Michał','Zieliński',NULL,'789012345678','michal.zielinski@example.com'),(8,'Agnieszka','Szymańska','ul. Wiejska 12, 08-008 Białystok','890123456789','agnieszka.szymanska@example.com'),(9,'Robert','Woźniak',NULL,'901234567890','robert.wozniak@example.com'),(10,'Joanna','Kozłowska','ul. Wiosenna 3, 10-010 Rzeszów','012345678901','joanna.kozlowska@example.com'),(11,'Ewa','Jankowska','ul. Lipowa 4, 11-011 Lublin','123456789013','ewa.jankowska@example.com'),(12,'Grzegorz','Król',NULL,'234567890124','grzegorz.krol@example.com'),(13,'Beata','Kaczmarek','ul. Długa 6, 12-012 Kraków','345678901235','beata.kaczmarek@example.com'),(14,'Dawid','Maj','ul. Leśna 7, 13-013 Katowice','456789012356','dawid.maj@example.com'),(15,'Natalia','Szulc','ul. Jasna 8, 14-014 Wrocław','567890123467','natalia.szulc@example.com'),(16,'Karol','Adamski',NULL,'678901234578','karol.adamski@example.com'),(17,'Marta','Zając','ul. Cicha 9, 15-015 Bydgoszcz','789012345689','marta.zajac@example.com'),(18,'Wojciech','Bąk','ul. Szkolna 10, 16-016 Gdynia','890123456790','wojciech.bak@example.com'),(19,'Julia','Lis','ul. Wesoła 11, 17-017 Toruń','901234567801','julia.lis@example.com'),(20,'Patryk','Kowalczyk','ul. Szeroka 12, 18-018 Olsztyn','012345678912','patryk.kowalczyk@example.com');
/*!40000 ALTER TABLE `readers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `librarian_id` int(11) DEFAULT NULL,
  `reader_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `librarian_id` (`librarian_id`),
  UNIQUE KEY `reader_id` (`reader_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`librarian_id`) REFERENCES `librarians` (`librarian_id`) ON DELETE CASCADE,
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`reader_id`) REFERENCES `readers` (`reader_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'jan_kowalski','haslo123',NULL,1),(2,'anna_nowak','anna123',NULL,2),(3,'piotr_wisniewski','p1otr12',NULL,3),(4,'katarzyna_wojcik','kw123',NULL,4),(5,'tomasz_kaminski','tomasz789',NULL,5),(6,'maria_lewandowska','haslo123',NULL,6),(7,'michal_zielinski','haslo123',NULL,7),(8,'agnieszka_szymanska','haslo123',NULL,8),(9,'robert_wozniak','haslo123',NULL,9),(10,'joanna_kozlowska','haslo123',NULL,10),(11,'ewa_jankowska','haslo123',NULL,11),(12,'grzegorz_krol','haslo123',NULL,12),(13,'beata_kaczmarek','haslo123',NULL,13),(14,'dawid_maj','haslo123',NULL,14),(15,'natalia_szulc','haslo123',NULL,15),(16,'karol_adamski','haslo123',NULL,16),(17,'marta_zajac','haslo123',NULL,17),(18,'wojciech_bak','haslo123',NULL,18),(19,'julia_lis','haslo123',NULL,19),(20,'patryk_kowalczyk','haslo123',NULL,20),(21,'alicja_kwiatkowska','alicja_pass',1,NULL),(22,'bartosz_nowicki','bartek123',2,NULL),(23,'1','1',3,NULL),(24,'damian_wojcik','damian123',4,NULL),(25,'elzbieta_kaminska','elzbieta987',5,NULL),(26,'karolina_zalewska','karolina123',6,NULL),(27,'marek_kowalczyk','marek123',7,NULL),(28,'anna_lewicka','anna_pass',8,NULL),(29,'jakub_majewski','jakub123',9,NULL),(30,'monika_koziol','monika123',10,NULL),(31,'pawel_nowak','pawel123',11,NULL),(32,'dorota_wisniewska','dorota123',12,NULL),(33,'jacek_wrobel','jacek123',13,NULL),(34,'magdalena_jankowska','magda123',14,NULL),(35,'rafal_kaczmarek','rafal123',15,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-03 21:59:43
