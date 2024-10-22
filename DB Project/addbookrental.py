# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox
import booksearch_2
import librarianpage
import usersearch
import mysql.connector
import mail


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\wikto\OneDrive\Pulpit\Bazy-Danych\DB Project\Assets\AddRentalPage")


# FUNCTIONS #
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def rent(list_user, list_book, rental_date_calendar, return_date_calendar, librarian_id, window):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    user_id = list_user[3]

    # Zapytanie SQL
    sql_query = "SELECT reader_id FROM Users WHERE user_id = %s;"

    # Wykonanie zapytania z przekazaniem wartości
    mycursor.execute(sql_query, (user_id,))

    # Pobranie wyników
    result = mycursor.fetchone()

    if result:
        reader_id = result[0]

    book_id = list_book[3]

    rent_date = rental_date_calendar.get()
    return_date = return_date_calendar.get()

    # Sprawdzenie, czy book_id występuje w tabeli BookRentals
    check_query = "SELECT COUNT(*) FROM BookRentals WHERE book_id = %s"
    mycursor.execute(check_query, (book_id,))
    count = mycursor.fetchone()[0]

    if return_date < rent_date:
        tkinter.messagebox.showinfo("Błąd danych", "Data zwrotu nie może być mniejsza niż data wypożyczenia!")
    elif count >= 1:
        tkinter.messagebox.showinfo("Błąd danych", "Wybrana książka została już wypożyczona!")
    elif list_user[0] == "":
        tkinter.messagebox.showinfo("Błąd danych", "Nie wybrano czytelnika!")
    elif list_book[0] == "":
        tkinter.messagebox.showinfo("Błąd danych", "Nie wybrano książki!")
    else:
        sql_query_2 = "INSERT INTO BookRentals (reader_id, book_id, rental_date, potential_return_date, librarian_id) VALUES (%s, %s, %s, %s, %s);"

        # Wykonanie zapytania z przekazaniem wartości
        mycursor.execute(sql_query_2, (reader_id, book_id, rent_date, return_date, librarian_id))

        # Zatwierdzenie zmian w bazie danych
        db.commit()

        tkinter.messagebox.showinfo("Komunikat", "Książka została wypożyczona")

        mail.send_email(1, list_user, list_book, return_date)

        back_to_librarian_page(window, librarian_id)


def book_search(window, text, mycursor, librarian_id, list_book, list_user):
    search_text = text.get()

    if search_text.isdigit():
        sql_query = "SELECT title, author, book_id FROM Books WHERE book_id = %s"
        mycursor.execute(sql_query, (int(search_text),))
    else:
        if ',' in search_text:
            title, author = map(str.strip, search_text.split(',', 1))
            sql_query = "SELECT title, author, book_id FROM Books WHERE title LIKE %s AND author LIKE %s"
            mycursor.execute(sql_query, (f"%{title}%", f"%{author}%"))
        else:
            sql_query = "SELECT title, author, book_id FROM Books WHERE title LIKE %s OR author LIKE %s"
            mycursor.execute(sql_query, (f"%{search_text}%", f"%{search_text}%"))

    results = mycursor.fetchall()

    window.destroy()

    new_window = Tk()
    new_window.title("Wyniki wyszukiwania - eAGH")
    new_window.geometry("1000x800")

    booksearch_2.show_search_page(new_window, results, librarian_id, list_book, list_user)


def reader_search(window, text, mycursor, librarian_id, list_book, list_user):
    search_text = text.get()

    if ' ' in search_text:
        name, surname = map(str.strip, search_text.split(' ', 1))
        sql_query = "SELECT Users.user_id, Readers.name, Readers.surname FROM Users JOIN Readers ON Users.reader_id = Readers.reader_id WHERE Readers.name LIKE %s AND Readers.surname LIKE %s"
        mycursor.execute(sql_query, (f"%{name}%", f"%{surname}%"))
    else:
        sql_query = "SELECT Users.user_id, Readers.name, Readers.surname FROM Users JOIN Readers ON Users.reader_id = Readers.reader_id WHERE Readers.name LIKE %s OR Readers.surname LIKE %s"
        mycursor.execute(sql_query, (f"%{search_text}%", f"%{search_text}%"))

    results = mycursor.fetchall()

    window.destroy()

    new_window = Tk()
    new_window.title("Wyniki wyszukiwania - eAGH")
    new_window.geometry("1000x800")

    usersearch.show_search_page(new_window, results, librarian_id, list_book, list_user)


def align_window(window):
    window_width = 1000
    window_height = 800

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")


def back_to_librarian_page(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Bibliotekarz - eAGH")
    new_window.geometry("1000x800")

    librarianpage.show_librarian_page(new_window, librarian_id)


def show_addrental_page(window, librarian_id, list_user, list_book):

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    if len(list_user) == 0:
        list_user.append("")
        list_user.append("")
        list_user.append("")
        list_user.append("")

    if len(list_book) == 0:
        list_book.append("")
        list_book.append("")
        list_book.append("")
        list_book.append("")

    align_window(window)

    canvas = Canvas(
        window,
        bg = "#00693C",
        height = 800,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        1.0,
        0.0,
        1001.0,
        800.0,
        fill="#108A56",
        outline="")

    canvas.create_rectangle(
        50.0,
        50.0,
        950.0,
        750.0,
        fill="#00693C",
        outline="")

    canvas.create_rectangle(
        106.0,
        95.0,
        893.0,
        705.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: rent(list_user, list_book, rental_date_calendar, return_date_calendar, librarian_id, window),
        relief="flat"
    )
    button_1.place(
        x=183.0,
        y=630.0,
        width=245.0,
        height=47.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_librarian_page(window, librarian_id),
        relief="flat"
    )
    button_2.place(
        x=568.0,
        y=630.0,
        width=245.0,
        height=47.0
    )

    canvas.create_rectangle(
        138.0,
        579.0,
        273.0,
        610.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        540.0,
        342.0,
        571.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        499.0,
        854.0,
        530.0,
        fill="#D9D9D9",
        outline="")

    rental_date_calendar = DateEntry(window, width=12, background='#A71930', foreground='white', borderwidth=5, showweeknumbers=False, date_pattern="yyyy-mm-dd")
    rental_date_calendar.place(x=342.0, y=540.0, width=512.0, height=31.0)

    return_date_calendar = DateEntry(window, width=12, background='#A71930', foreground='white', borderwidth=5, showweeknumbers=False, date_pattern="yyyy-mm-dd")
    return_date_calendar.place(x=272.0, y=579.0, width=582.0, height=31.0)

    canvas.create_rectangle(
        138.0,
        459.0,
        854.0,
        490.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        419.0,
        854.0,
        450.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        379.0,
        854.0,
        410.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        299.0,
        854.0,
        330.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        339.0,
        854.0,
        370.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        193.0,
        305.0,
        anchor="nw",
        text=f"{list_user[0]}",
        fill="#000000",
        font=("Inter 12")
    )

    canvas.create_text(
        247.0,
        345.0,
        anchor="nw",
        text=f"{list_user[1]}",
        fill="#000000",
        font=("Inter 12")
    )

    canvas.create_text(
        213.0,
        385.0,
        anchor="nw",
        text=f"{list_user[2]}",
        fill="#000000",
        font=("Inter 12")
    )

    canvas.create_text(
        204.0,
        424.0,
        anchor="nw",
        text=f"{list_book[0]}",
        fill="#000000",
        font=("Inter 12")
    )

    canvas.create_text(
        209.0,
        464.0,
        anchor="nw",
        text=f"{list_book[1]}",
        fill="#000000",
        font=("Inter 12")
    )

    canvas.create_text(
        249.0,
        505.0,
        anchor="nw",
        text=f"{list_book[2]}",
        fill="#000000",
        font=("Inter 12")
    )

    canvas.create_text(
        141.0,
        342.0,
        anchor="nw",
        text=f"Nazwisko: ",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        383.0,
        anchor="nw",
        text="Adres:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        422.0,
        anchor="nw",
        text="Tytuł:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        462.0,
        anchor="nw",
        text="Autor:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        502.0,
        anchor="nw",
        text="Wydawca:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        543.0,
        anchor="nw",
        text="Data wypożyczenia:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        581.0,
        anchor="nw",
        text="Data zwrotu:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        141.0,
        302.0,
        anchor="nw",
        text="Imię:",
        fill="#000000",
        font=("Inter Medium", 20 * -1)
    )

    canvas.create_text(
        355.0,
        120.0,
        anchor="nw",
        text="Panel wypożyczeń",
        fill="#000000",
        font=("Inter SemiBold", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        855.0,
        151.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        179.0,
        187.0,
        214.0,
        222.0,
        fill="#118A56",
        outline="")

    canvas.create_rectangle(
        179.0,
        240.0,
        214.0,
        275.0,
        fill="#118A56",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        478.5,
        204.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#EBEBEB",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=214.0,
        y=187.0,
        width=529.0,
        height=33.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        478.5,
        257.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#EBEBEB",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=214.0,
        y=240.0,
        width=529.0,
        height=33.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        196.0,
        257.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        196.0,
        204.0,
        image=image_image_3
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: book_search(window, entry_1, mycursor, librarian_id, list_book, list_user),
        relief="flat"
    )
    button_3.place(
        x=743.0,
        y=187.0,
        width=70.0,
        height=35.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: reader_search(window, entry_2, mycursor, librarian_id, list_book, list_user),
        relief="flat"
    )
    button_4.place(
        x=743.0,
        y=240.0,
        width=70.0,
        height=35.0
    )
    window.resizable(False, False)
    window.mainloop()
