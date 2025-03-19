# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.messagebox
import librarianpage
import mysql.connector
import random
import string


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "Assets" / "AddReaderPage"

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


def random_data_generator(db, mycursor, name, surname, reader_id):
    username = name + "_" + surname

    status = False

    while status != True:
        check_query = "SELECT COUNT(*) FROM Users WHERE username = %s"
        mycursor.execute(check_query, (username,))
        count = mycursor.fetchone()[0]

        if count >= 1:
            username = name + "_" + surname + str(random.randint(0, 100))
        else:
            status = True

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(random.randint(7, 10)))

    sql_query = "INSERT INTO Users (username, password, librarian_id, reader_id) VALUES (%s, %s, %s, %s)"
    values = (username, password, None, reader_id[0])
    mycursor.execute(sql_query, values)
    db.commit()

    return username, password


def back_to_librarianpage(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Librarian")
    new_window.geometry("1000x800")

    librarianpage.show_librarian_page(new_window, librarian_id)


def add_user(n, s, a, t, e, window, librarian_id):
    name = n.get()
    surname = s.get()
    address = a.get()
    telephone_number = t.get()
    email = e.get()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    check_query = "SELECT COUNT(*) FROM Readers WHERE email = %s"
    mycursor.execute(check_query, (email,))
    count = mycursor.fetchone()[0]

    main_occur = False

    if count >= 1:
        main_occur = True

    if len(name) == 0:
        tkinter.messagebox.showinfo("Data error", "Wrong name!")
    elif len(surname) == 0:
        tkinter.messagebox.showinfo("Data error", "Wrong surname!")
    elif len(telephone_number) == 0 or telephone_number.isdigit() == False:
        tkinter.messagebox.showinfo("Data error", "Incorrect phone number!")
    elif main_occur is True:
        tkinter.messagebox.showinfo("Data error", "The email address provided already belongs to another reader!")
    else:
        sql_query = "INSERT INTO Readers (name, surname, address, phone_number, email) VALUES (%s, %s, %s, %s, %s)"
        values = (name, surname, address, telephone_number, email)
        mycursor.execute(sql_query, values)
        db.commit()

        sql_query_2 = "SELECT reader_id FROM Readers WHERE name = %s AND surname = %s AND address = %s AND phone_number = %s AND email = %s"
        mycursor.execute(sql_query_2, (name, surname, address, telephone_number, email))
        reader_id = mycursor.fetchone()

        username, password = random_data_generator(db, mycursor, name, surname, reader_id)

        tkinter.messagebox.showinfo("Announcement", "Reader has been added")
        tkinter.messagebox.showinfo("Login details", f"Username: {username}\nPassword: {password}")

        back_to_librarianpage(window, librarian_id)


def show_addreader_page(window, librarian_id):
    align_window(window)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    canvas = Canvas(
        window,
        bg = "#118A56",
        height = 800,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        50.0,
        50.0,
        950.0,
        750.0,
        fill="#00693C",
        outline="")

    canvas.create_rectangle(
        106.0,
        116.0,
        893.0,
        683.0,
        fill="#ECECEC",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        855.0,
        160.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        138.0,
        281.0,
        221.0,
        329.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        391.0,
        233.0,
        439.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        446.0,
        343.0,
        494.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        501.0,
        225.0,
        549.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        336.0,
        277.0,
        384.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        522.0,
        304.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter 12")
    )
    entry_1.place(
        x=209.0,
        y=281.0,
        width=626.0,
        height=45.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        554.5,
        359.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter 12")
    )
    entry_2.place(
        x=274.0,
        y=336.0,
        width=561.0,
        height=45.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        532.0,
        414.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter 12")
    )
    entry_3.place(
        x=229.0,
        y=391.0,
        width=606.0,
        height=45.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        589.0,
        469.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter 12")
    )
    entry_4.place(
        x=343.0,
        y=446.0,
        width=492.0,
        height=45.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        530.0,
        524.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Inter 12")
    )
    entry_5.place(
        x=225.0,
        y=501.0,
        width=610.0,
        height=45.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_librarianpage(window, librarian_id),
        relief="flat"
    )
    button_1.place(
        x=561.0,
        y=584.0,
        width=245.0,
        height=47.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_user(entry_1, entry_2, entry_3, entry_4, entry_5, window, librarian_id),
        relief="flat"
    )
    button_2.place(
        x=179.0,
        y=584.0,
        width=245.0,
        height=47.0
    )

    canvas.create_text(
        145.0,
        289.0,
        anchor="nw",
        text="Name:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        345.0,
        anchor="nw",
        text="Surname:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        454.0,
        anchor="nw",
        text="Phone number:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        508.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        399.0,
        anchor="nw",
        text="Address: ",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        362.0,
        148.0,
        anchor="nw",
        text="Add a reader",
        fill="#000000",
        font=("Inter Black", 32 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
