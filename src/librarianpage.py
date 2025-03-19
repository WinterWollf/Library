# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import tkinter.messagebox
import mysql.connector
import backup
import addbookreturn
import booksearch
import addreader
import addbook
import addbookrental
import qrcodegenereator
import subprocess
import raportapage


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "Assets" / "LibrarianPage"

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


def log_out(window):
    window.destroy()

    tkinter.messagebox.showinfo("Announcement", "You have been successfully logged out of the system")


def make_backup(security_level):
    if security_level == 3:
        text = backup.make_backup()
        tkinter.messagebox.showinfo("Announcement", f"Successfully backed up the database to a file {text}")
    else:
        tkinter.messagebox.showinfo("Refusal", f"No permissions to create backup")


def get_top_readers(mycursor):
    sql_query = "SELECT Readers.name, Readers.surname, COUNT(History.history_id) AS rentals_count FROM History JOIN Readers ON History.user_id = (SELECT user_id FROM Users WHERE reader_id = Readers.reader_id) GROUP BY Readers.reader_id ORDER BY rentals_count DESC LIMIT 3;"
    mycursor.execute(sql_query)
    top_readers = mycursor.fetchall()
    return top_readers


def search(window, text, mycursor, librarian_id):
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
    new_window.title("Search results")
    new_window.geometry("1000x800")

    booksearch.show_search_page(new_window, results, librarian_id)


def add_reader(window, librarian_id, security_level):
    if security_level >= 2:
        window.destroy()

        new_window = Tk()
        new_window.title("Adding a new reader")
        new_window.geometry("1000x800")

        addreader.show_addreader_page(new_window, librarian_id)
    else:
        tkinter.messagebox.showinfo("Refusal", f"No permissions to add new readers")


def add_book(window, librarian_id, security_level):
    if security_level >= 2:
        window.destroy()

        new_window = Tk()
        new_window.title("Adding a new item")
        new_window.geometry("1000x800")

        tablica = ["", "", "", "", "", "", ""]

        addbook.show_add_book_page(new_window, librarian_id, tablica)
    else:
        tkinter.messagebox.showinfo("Refusal", f"No permissions to add new books")


def add_rental(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Adding a new rental")
    new_window.geometry("1000x800")

    addbookrental.show_addrental_page(new_window, librarian_id, [], [])


def add_return(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Adding a new rental")
    new_window.geometry("1000x800")

    addbookreturn.show_addreturn_page(new_window, librarian_id, [], [])


def generate_qr_code(security_level):
    if security_level >= 2:
        qrcodegenereator.generate_qr_codes("QR_CODES.pdf")
        pdf_path = "QR_CODES.pdf"

        try:
            subprocess.run(['xdg-open', pdf_path], check=True)  # Dla systemów opartych na Linuksie
        except FileNotFoundError:
            try:
                subprocess.run(['open', pdf_path], check=True)  # Dla systemu macOS
            except FileNotFoundError:
                try:
                    subprocess.run(['start', '', pdf_path], check=True, shell=True)  # Dla systemu Windows
                except FileNotFoundError:
                    tkinter.messagebox.showinfo("Error", "An error occurred while generating the file!")
    else:
        tkinter.messagebox.showinfo("Refusal", f"No permissions required to generate QR codes")


def raport_page(window, librarian_id, security_level):
    if security_level == 3:
        window.destroy()

        window = Tk()
        window.title("Report Generator")
        window.geometry("1000x800")

        raportapage.show_raport_page(window, librarian_id)
    else:
        tkinter.messagebox.showinfo("Refusal", f"No permissions required to generate reports")


def show_librarian_page(window, librarian_id):
    align_window(window)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    top_readers = get_top_readers(mycursor)

    sql_query = "SELECT name, surname, security_level FROM Librarians WHERE librarian_id = %s"
    mycursor.execute(sql_query, (librarian_id,))
    librarian = mycursor.fetchone()

    name, surname, security_level = librarian

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

    canvas.create_rectangle(
        582.0,
        369.0,
        843.0,
        623.0,
        fill="#EBEBEB",
        outline="")

    canvas.create_rectangle(
        583.0,
        452.0,
        843.0,
        482.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        583.0,
        503.0,
        843.0,
        533.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        583.0,
        554.0,
        843.0,
        584.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        179.0,
        277.0,
        214.0,
        312.0,
        fill="#118A56",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))

    entry_bg_1 = canvas.create_image(
        478.5,
        294.5,
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
        y=277.0,
        width=529.0,
        height=33.0
    )

    canvas.create_text(
        107.0,
        92.0,
        anchor="nw",
        text=f"Welcome {name} {surname}!",
        fill="#FFFFFF",
        font=("Inter SemiBold", 32 * -1)
    )

    canvas.create_text(
        355.0,
        204.0,
        anchor="nw",
        text="Management panel",
        fill="#000000",
        font=("Inter SemiBold", 32 * -1)
    )

    canvas.create_text(
        622.0,
        396.0,
        anchor="nw",
        text="Reader ranking",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        600.0,
        455.0,
        anchor="nw",
        text=f"1. {top_readers[0][0]} {top_readers[0][1]}, {top_readers[0][2]}",
        fill="#000000",
        font=("Inter Black", 20 * -1)
    )

    canvas.create_text(
        600.0,
        505.0,
        anchor="nw",
        text=f"2. {top_readers[1][0]} {top_readers[1][1]}, {top_readers[1][2]}",
        fill="#000000",
        font=("Inter Black", 20 * -1)
    )

    canvas.create_text(
        600.0,
        557.0,
        anchor="nw",
        text=f"3. {top_readers[2][0]} {top_readers[2][1]}, {top_readers[2][2]}",
        fill="#000000",
        font=("Inter Black", 20 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))

    image_1 = canvas.create_image(
        196.0,
        294.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))

    image_2 = canvas.create_image(
        854.0,
        223.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: search(window, entry_1, mycursor, librarian_id),
        relief="flat"
    )

    button_1.place(
        x=743.0,
        y=277.0,
        width=70.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_rental(window, librarian_id),
        relief="flat"
    )

    button_2.place(
        x=149.0,
        y=347.0,
        width=182.0,
        height=33.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))

    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_reader(window, librarian_id, security_level),
        relief="flat"
    )

    button_3.place(
        x=149.0,
        y=399.0,
        width=182.0,
        height=33.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))

    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_book(window, librarian_id, security_level),
        relief="flat"
    )

    button_4.place(
        x=149.0,
        y=451.0,
        width=182.0,
        height=33.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))

    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: generate_qr_code(security_level),
        relief="flat"
    )

    button_5.place(
        x=149.0,
        y=503.0,
        width=182.0,
        height=33.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))

    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: raport_page(window, librarian_id, security_level),
        relief="flat"
    )

    button_6.place(
        x=149.0,
        y=555.0,
        width=182.0,
        height=33.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))

    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_return(window, librarian_id),
        relief="flat"
    )

    button_7.place(
        x=149.0,
        y=607.0,
        width=182.0,
        height=33.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: log_out(window),
        relief="flat"
    )
    button_8.place(
        x=898.0,
        y=60.0,
        width=45.0,
        height=45.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: make_backup(security_level),
        relief="flat"
    )
    button_9.place(
        x=834.0,
        y=60.0,
        width=45.0,
        height=45.0
    )

    window.resizable(False, False)
    window.mainloop()
