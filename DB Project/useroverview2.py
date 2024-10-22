# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import usersearch2
import addbookreturn
import mysql.connector


# PATHS
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\wikto\OneDrive\Pulpit\Bazy-Danych\DB Project\Assets\UserOverView")


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


def back_to_serach_page(window, result, librarian_id, list_book, list_user):
    window.destroy()

    new_window = Tk()
    new_window.title("Wyniki wyszukiwania - eAGH")
    new_window.geometry("1000x800")

    usersearch2.show_search_page(new_window, result, librarian_id, list_book, list_user)


def return_date(window, librarian_id, list_book, list_user):
    window.destroy()

    new_window = Tk()
    new_window.title("Dodawanie nowego wypożyczenia - eAGH")
    new_window.geometry("1000x800")

    addbookreturn.show_addreturn_page(new_window, librarian_id, list_user, list_book)


def show_user_overview(window, user_id, result, librarian_id, list_book, list_user):
    align_window(window)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    sql_query = "SELECT Readers.name, Readers.surname, Readers.address, Readers.phone_number, Readers.email FROM Users JOIN Readers ON Users.reader_id = Readers.reader_id WHERE Users.user_id = %s"
    mycursor.execute(sql_query, (user_id,))
    reader = mycursor.fetchone()

    if reader:
        name, surname, address, telephone_numer, email = reader
    else:
        print("Error")

    if address == None:
        address = "Brak danych"
    else:
        parts = address.split(', ')
        street = parts[0]
        postal_code_and_city = parts[1]

        # Dalszy podział na kod pocztowy i miasto
        postal_code, address = map(str.strip, postal_code_and_city.split(' ', 1))

    if email == None:
        address = "Brak danych"

    list_user_temporary = [name, surname, address, user_id]

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
        107.0,
        117.0,
        894.0,
        684.0,
        fill="#EBEBEB",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: return_date(window, librarian_id, list_book, list_user_temporary),
        relief="flat"
    )
    button_1.place(
        x=443.0,
        y=609.0,
        width=184.0,
        height=47.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_serach_page(window, result, librarian_id, list_book, list_user),
        relief="flat"
    )
    button_2.place(
        x=667.0,
        y=609.0,
        width=184.0,
        height=47.0
    )

    canvas.create_rectangle(
        151.0,
        268.0,
        499.0,
        571.0,
        fill="#D9D9D9",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        851.0,
        161.0,
        image=image_image_1
    )

    canvas.create_text(
        405.0,
        139.0,
        anchor="nw",
        text=f"{name} {surname}",
        fill="#A71930",
        font=("Inter Black", 30 * -1)
    )

    canvas.create_text(
        170.0,
        399.0,
        anchor="nw",
        text=f"{address}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        170.0,
        452.0,
        anchor="nw",
        text=f"{telephone_numer}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        170.0,
        505.0,
        anchor="nw",
        text=f"{email}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        170.0,
        294.0,
        anchor="nw",
        text=f"{name}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        170.0,
        346.0,
        anchor="nw",
        text=f"{surname}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        648.0,
        399.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()
