import pymysql
import subprocess
import os
import datetime


def make_backup():
    # Dane dostępowe do bazy danych
    user = 'root'
    host = 'localhost'
    database = 'library'

    # Ścieżka, gdzie ma zostać zapisany plik
    backup_dir = r'C:\Users\wikto\OneDrive\Pulpit\Bazy-Danych\DB Project\BackUp'

    # Ścieżka do mysqldump
    mysqldump_path = r'C:\xampp\mysql\bin\mysqldump.exe'  # zmień na odpowiednią ścieżkę

    # Tworzenie nazwy pliku na podstawie daty
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = f'{database}_{current_time}.sql'
    backup_file = os.path.join(backup_dir, name)

    try:
        # Łączenie z bazą danych
        connection = pymysql.connect(host=host, user=user, database=database)

        # Tworzenie kursora
        cursor = connection.cursor()

        # Wykonanie polecenia SQL do uzyskania kopii zapasowej bazy danych
        with open(backup_file, 'w') as f:
            subprocess.Popen([mysqldump_path, '-u', user, '-h', host, database], stdout=f)

        print("Kopia zapasowa została zapisana w:", backup_file)

    except pymysql.Error as e:
        print("Wystąpił błąd podczas wykonywania kopii zapasowej:", e)

    finally:
        # Zamykanie połączenia
        if connection:
            connection.close()

    return name
