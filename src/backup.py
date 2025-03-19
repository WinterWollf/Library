import pymysql
import subprocess
import os
import datetime
from pathlib import Path


def make_backup():
    user = 'root'
    host = 'localhost'
    database = 'library'

    OUTPUT_PATH = Path(__file__).parent
    backup_dir = OUTPUT_PATH / "BackUp"

    mysqldump_path = r'C:\xampp\mysql\bin\mysqldump.exe'  # zmień na odpowiednią ścieżkę

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = f'{database}_{current_time}.sql'
    backup_file = os.path.join(backup_dir, name)

    try:
        connection = pymysql.connect(host=host, user=user, database=database)
        cursor = connection.cursor()

        with open(backup_file, 'w') as f:
            subprocess.Popen([mysqldump_path, '-u', user, '-h', host, database], stdout=f)

        print("The backup copy was saved in:", backup_file)

    except pymysql.Error as e:
        print("An error occurred while performing backup:", e)

    finally:
        if connection:
            connection.close()

    return name
