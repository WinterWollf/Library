# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import tkinter.messagebox
import mysql.connector
import librarianpage
import readerpage


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "Assets" / "LoginPage"


# FUNCTIONS #
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def align_window():
    window_width = 1000
    window_height = 800

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")


def check_data():
    username = entry_1.get()
    password = entry_2.get()

    # Utwórz połączenie z bazą danych
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    sql_query = "SELECT user_id, librarian_id, reader_id FROM Users WHERE username = %s AND password = %s"
    mycursor.execute(sql_query, (username, password))
    user = mycursor.fetchone()

    if user:
        user_id, librarian_id, reader_id = user

        if librarian_id is not None:
            print("Login successful!")

            window.destroy()

            new_window = Tk()

            new_window.title("Librarian")
            new_window.geometry("1000x800")

            librarianpage.show_librarian_page(new_window, librarian_id)
        elif reader_id is not None:
            print("Access denied")
            tkinter.messagebox.showinfo("Announcement", "Service login error! Use student page!")
        else:
            print("User is neither a librarian nor a reader.")
    else:
        tkinter.messagebox.showinfo("Data error", "Incorrect data entered!")

    mycursor.close()
    db.close()


window = Tk()

window.title("Login to the library system")
window.geometry("1000x800")
window.configure(bg="#00693C")
align_window()

# CANVAS #
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
    113.0,
    146.0,
    454.0,
    655.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    215.0,
    168.0,
    anchor="nw",
    text="Welcome",
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

canvas.create_text(
    130.0,
    407.0,
    anchor="nw",
    text="Log in to your account",
    fill="#00693C",
    font=("Inter SemiBold", 12 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))

image_1 = canvas.create_image(
    283.0,
    303.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))

entry_bg_1 = canvas.create_image(
    283.5,
    451.5,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter 12")
)

entry_1.place(
    x=129.0,
    y=428.0,
    width=309.0,
    height=45.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))

entry_bg_2 = canvas.create_image(
    283.5,
    516.5,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show="*",
    width=20,
    font=("Inter 12")
)

entry_2.place(
    x=129.0,
    y=493.0,
    width=309.0,
    height=45.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_data,
    relief="flat"
)

button_1.place(
    x=161.0,
    y=574.0,
    width=245.0,
    height=47.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))

image_2 = canvas.create_image(
    710.0,
    380.0,
    image=image_image_2
)

window.resizable(False, False)
window.mainloop()
