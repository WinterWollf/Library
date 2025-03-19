# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import librarianpage
import booksearch_4
import usersearch3
import mysql.connector
from datetime import datetime


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "Assets" / "RaportPage"


# FUNCTIONS #
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def align_window(window):
    window_width = 1000
    window_height = 800

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")


def show_librarian_page(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Librarian")
    new_window.geometry("1000x800")

    librarianpage.show_librarian_page(new_window, librarian_id)


def current_rented_books(window, librarian_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    query = "SELECT Books.title, Books.author, Books.book_id FROM BookRentals JOIN Books ON BookRentals.book_id = Books.book_id"

    mycursor.execute(query)
    rented_books = mycursor.fetchall()

    window.destroy()

    new_window = Tk()
    new_window.title("Report")
    new_window.geometry("1000x800")

    booksearch_4.show_search_page(new_window, librarian_id, rented_books)


def most_rented_books(window, librarian_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    query = "SELECT Books.title, Books.author, Books.book_id, COUNT(History.book_id) AS rental_count FROM History JOIN Books ON History.book_id = Books.book_id GROUP BY History.book_id, Books.title, Books.author ORDER BY rental_count DESC;"

    mycursor.execute(query)
    most_read_books = mycursor.fetchall()

    window.destroy()

    new_window = Tk()
    new_window.title("Report")
    new_window.geometry("1000x800")
    booksearch_4.show_search_page(new_window, librarian_id, most_read_books)


def most_active_readers(window, librarian_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    query ="SELECT History.user_id, Readers.name, Readers.surname, COUNT(History.user_id) AS rental_count FROM History JOIN Users ON History.user_id = Users.user_id JOIN Readers ON Users.reader_id = Readers.reader_id GROUP BY History.user_id, Readers.name, Readers.surname ORDER BY rental_count DESC;"
    mycursor.execute(query)
    most_active = mycursor.fetchall()

    status = 1

    window.destroy()

    new_window = Tk()
    new_window.title("Report")
    new_window.geometry("1000x800")

    usersearch3.show_search_page(new_window, librarian_id, most_active, status)


def readers(window, librarian_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    query = "SELECT Users.user_id, Readers.name, Readers.surname FROM Users JOIN Readers ON Users.reader_id = Readers.reader_id"

    mycursor.execute(query)
    readers_list = mycursor.fetchall()

    status = 2

    window.destroy()

    new_window = Tk()
    new_window.title("Report")
    new_window.geometry("1000x800")

    usersearch3.show_search_page(new_window, librarian_id, readers_list, status)


def readers_with_overdue_books(window, librarian_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    query = """
    SELECT
        Users.user_id,
        Readers.name,
        Readers.surname,
        Books.title,
        Books.author,
        DATEDIFF(CURRENT_DATE, BookRentals.potential_return_date) AS days_late
    FROM
        BookRentals
    JOIN
        Users ON BookRentals.reader_id = Users.reader_id
    JOIN
        Readers ON Users.reader_id = Readers.reader_id
    JOIN
        Books ON BookRentals.book_id = Books.book_id
    WHERE
        BookRentals.potential_return_date < %s
        AND BookRentals.potential_return_date < CURRENT_DATE;
    """

    date_str = datetime.now().strftime('%Y-%m-%d')

    mycursor.execute(query, (date_str,))

    overdue_books = mycursor.fetchall()

    status = 3

    window.destroy()

    new_window = Tk()
    new_window.title("Report")
    new_window.geometry("1000x800")

    usersearch3.show_search_page(new_window, librarian_id, overdue_books, status)


def late_rentes(window, librarian_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    query = """
    SELECT 
        h.user_id,
        CASE 
            WHEN u.reader_id IS NOT NULL THEN r.name
            ELSE l.name
        END AS name,
        CASE 
            WHEN u.reader_id IS NOT NULL THEN r.surname
            ELSE l.surname
        END AS surname,
        b.title,
        b.author,
        DATEDIFF(h.date_of_return, h.potential_return_date) AS days_late
    FROM 
        History h
    JOIN 
        Users u ON h.user_id = u.user_id
    LEFT JOIN 
        Readers r ON u.reader_id = r.reader_id
    LEFT JOIN 
        Librarians l ON u.librarian_id = l.librarian_id
    JOIN 
        Books b ON h.book_id = b.book_id
    WHERE 
        h.belated = 1;
    """

    mycursor.execute(query)
    overdue_books = mycursor.fetchall()

    status = 3

    window.destroy()

    new_window = Tk()
    new_window.title("Report")
    new_window.geometry("1000x800")

    usersearch3.show_search_page(new_window, librarian_id, overdue_books, status)


def show_raport_page(window, librarian_id):
    align_window(window)

    canvas = Canvas(
        window,
        bg="#00693C",
        height=800,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        1.0,
        0.0,
        1001.0,
        800.0,
        fill="#108A56",
        outline="")

    canvas.create_rectangle(
        51.0,
        50.0,
        951.0,
        750.0,
        fill="#00693C",
        outline="")

    canvas.create_rectangle(
        103.0,
        180.0,
        890.0,
        682.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        383.0,
        225.0,
        anchor="nw",
        text="Generate report",
        fill="#000000",
        font=("Inter SemiBold", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        854.0,
        223.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: readers_with_overdue_books(window, librarian_id),
        relief="flat"
    )
    button_1.place(
        x=513.0,
        y=412.0,
        width=298.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: readers(window, librarian_id),
        relief="flat"
    )
    button_2.place(
        x=513.0,
        y=360.0,
        width=298.0,
        height=33.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: current_rented_books(window, librarian_id),
        relief="flat"
    )
    button_3.place(
        x=182.0,
        y=360.0,
        width=298.0,
        height=33.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: most_rented_books(window, librarian_id),
        relief="flat"
    )
    button_4.place(
        x=182.0,
        y=412.0,
        width=298.0,
        height=33.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: late_rentes(window, librarian_id),
        relief="flat"
    )
    button_5.place(
        x=513.0,
        y=464.0,
        width=298.0,
        height=33.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: most_active_readers(window, librarian_id),
        relief="flat"
    )
    button_6.place(
        x=182.0,
        y=464.0,
        width=298.0,
        height=33.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_librarian_page(window, librarian_id),
        relief="flat"
    )
    button_7.place(
        x=403.0,
        y=593.0,
        width=186.0,
        height=45.0
    )
    window.resizable(False, False)
    window.mainloop()
