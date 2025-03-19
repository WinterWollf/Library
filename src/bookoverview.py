# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "Assets" / "BookSearch"
COVER_PATH = OUTPUT_PATH / "Assets" / "BookSearch" / "Covers"

# FUNCTIONS #
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def relative_to_covers(path: str) -> Path:
    return COVER_PATH / Path(path)


def align_window(window):
    window_width = 1000
    window_height = 800

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")


def show_book_overview(window, book_id):
    align_window(window)

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    sql_query = "SELECT b.title, b.author, b.release_date, b.publishing_house, g.genre_name, b.price FROM Books b JOIN BookGenres g ON b.book_genre_id = g.genre_id WHERE b.book_id = %s"
    mycursor.execute(sql_query, (book_id,))
    book = mycursor.fetchone()

    if book:
        title, author, release_date, publishing_house, book_genre_id, price = book
    else:
        print("Error")

    check_query = "SELECT COUNT(*) FROM BookRentals WHERE book_id = %s"
    mycursor.execute(check_query, (book_id,))
    count = mycursor.fetchone()[0]

    status = "Available"

    if count == 1:
        status = "Borrowed"

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
        116.0,
        894.0,
        683.0,
        fill="#EBEBEB",
        outline="")

    canvas.create_rectangle(
        591.0,
        242.0,
        843.0,
        648.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        617.0,
        425.0,
        anchor="nw",
        text=f"{publishing_house}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        617.0,
        478.0,
        anchor="nw",
        text=f"{book_genre_id}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        617.0,
        531.0,
        anchor="nw",
        text=f"{price}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        617.0,
        584.0,
        anchor="nw",
        text=f"{status}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        851.0,
        161.0,
        image=image_image_1
    )

    sql_query_cover = "SELECT path FROM BooksCovers c JOIN Books b ON b.book_id = c.book_id WHERE b.book_id = %s"
    mycursor.execute(sql_query_cover, (book_id,))
    cover_value = mycursor.fetchone()

    if cover_value == None:
        cover = cover_value
    else:
        cover = cover_value[0]

    if cover != None:
        image_image_2 = PhotoImage(
            file=relative_to_covers(cover))
        image_2 = canvas.create_image(
            360.0,
            400.0,
            image=image_image_2
        )
    else:
        image_image_2 = PhotoImage(
            file=relative_to_covers("book.png"))
        image_2 = canvas.create_image(
            360.0,
            400.0,
            image=image_image_2
        )

    canvas.create_text(
        403.0,
        152.0,
        anchor="nw",
        text=f"{title}",
        fill="#A71930",
        font=("Inter Black", 30 * -1)
    )

    canvas.create_text(
        617.0,
        267.0,
        anchor="nw",
        text=f"{title}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        617.0,
        319.0,
        anchor="nw",
        text=f"{author}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )

    canvas.create_text(
        617.0,
        372.0,
        anchor="nw",
        text=f"{release_date}",
        fill="#000000",
        font=("Inter Black", 22 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
