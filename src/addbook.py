# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
from tkcalendar import Calendar, DateEntry
import datetime
import tkinter.messagebox
from tkinter import ttk
import librarianpage
import mysql.connector
import booksearch_5


# PATHS #
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "Assets" / "AddBookPage"


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


def book_search(window, text, mycursor, librarian_id):
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

    booksearch_5.show_search_page(new_window, librarian_id, results)


def back_to_librarianpage(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Librarian")
    new_window.geometry("1000x800")

    librarianpage.show_librarian_page(new_window, librarian_id)


def get_genre_names(mycursor):
    mycursor.execute("SELECT genre_name FROM BookGenres")
    result = mycursor.fetchall()
    return [row[0] for row in result]


def get_genre_id(mycursor, genre_name):
    mycursor.execute("SELECT genre_id FROM BookGenres WHERE genre_name = %s", (genre_name,))
    result = mycursor.fetchone()
    return result[0] if result else None


def is_valid_price(price):
    try:
        float(price)
        return True
    except ValueError:
        return False


def add_book(t, a, r, p, g, pr, window, librarian_id, book_id):
    title = t.get()
    author = a.get()
    release_date = r.get()
    publishing_house = p.get()
    book_genre_name = g.get()
    price = pr.get()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    # Pobierz aktualną datę
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    if len(title) == 0:
        tkinter.messagebox.showinfo("Data error", "Wrong title!")
    elif len(author) == 0:
        tkinter.messagebox.showinfo("Data error", "Wrong author!")
    elif release_date > current_date:
        tkinter.messagebox.showinfo("Data error", "Incorrect release date!")
    elif not is_valid_price(price):
        tkinter.messagebox.showinfo("Data error", "Wrong price!")
    else:
        book_genre_id = get_genre_id(mycursor, book_genre_name)
        if book_genre_id is None:
            tkinter.messagebox.showinfo("Data error", "Wrong book genre!")
            return

        if book_id == 0:
            sql_query = "INSERT INTO Books (author, title, release_date, publishing_house, book_genre_id, price) VALUES (%s, %s, %s, %s, %s, %s)"

            values = (author, title, release_date, publishing_house, book_genre_id, price)

            mycursor.execute(sql_query, values)
            db.commit()

            tkinter.messagebox.showinfo("Announcement", "The book has been added successfully")
            back_to_librarianpage(window, librarian_id)
        else:
            sql_query = """
                UPDATE Books 
                SET author = %s, title = %s, release_date = %s, publishing_house = %s, book_genre_id = %s, price = %s 
                WHERE book_id = %s
            """

            values = (author, title, release_date, publishing_house, book_genre_id, price, book_id)

            mycursor.execute(sql_query, values)
            db.commit()

            tkinter.messagebox.showinfo("Announcement", "Book data has been successfully updated")
            back_to_librarianpage(window, librarian_id)


def show_add_book_page(window, librarian_id, book_data):
    align_window(window)

    if book_data[0] == "":
        book_data[6] = 0

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    mycursor = db.cursor()

    canvas = Canvas(
        window,
        bg="#118A56",
        height=800,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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
        231.0,
        221.0,
        279.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        342.0,
        326.0,
        389.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        396.0,
        285.0,
        444.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        506.0,
        223.0,
        554.0,
        fill="#D9D9D9",
        outline="")

    genres = get_genre_names(mycursor)
    selected_genre = StringVar()

    # if book_data[5] != 0:
    #     sql_quary_genre = "SELECT genre_id FROM BookGenres WHERE genre_name = %s"
    #     mycursor.execute(sql_quary_genre, (book_data[5],))
    #     results = mycursor.fetchone()
    #
    #     zmienna = results
    #
    #     print(zmienna)
    #
    #     selected_genre.set(genres[0])
    # else:
    selected_genre.set(genres[0])

    genre_combobox = ttk.Combobox(window, textvariable=selected_genre, values=genres, state='readonly',
                                  style='TCombobox')
    genre_combobox.place(x=277.0, y=451.0, width=558.0, height=45.0)
    genre_combobox.config(font=("Inter Medium", 15))

    canvas.create_rectangle(
        138.0,
        451.0,
        272.0,
        498.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        138.0,
        286.0,
        277.0,
        334.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        526.5,
        254.5,
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
        x=218.0,
        y=231.0,
        width=617.0,
        height=45.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        532.0,
        309.5,
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
        x=229.0,
        y=286.0,
        width=606.0,
        height=45.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        578.0,
        364.5,
        image=entry_image_3
    )

    if book_data[4] == "":
        default_date = "2024-06-15"
    else:
        default_date = str(book_data[4])

    default_date_obj = datetime.datetime.strptime(default_date, "%Y-%m-%d")

    rental_date_calendar = DateEntry(
        window,
        width=12,
        background='#A71930',
        foreground='white',
        borderwidth=5,
        showweeknumbers=False,
        date_pattern="yyyy-mm-dd",
        year=default_date_obj.year,
        month=default_date_obj.month,
        day=default_date_obj.day
    )
    rental_date_calendar.place(x=310.0, y=342.0, width=525.0, height=47.0)

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        556.0,
        419.5,
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
        x=277.0,
        y=396.0,
        width=558.0,
        height=45.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        527.5,
        529.5,
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
        x=220.0,
        y=506.0,
        width=615.0,
        height=45.0
    )

    entry_1.insert(0, book_data[0])
    entry_2.insert(0, book_data[1])
    entry_4.insert(0, str(book_data[2]))

    print(book_data)

    entry_5.insert(0, str(book_data[3]))


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
        command=lambda: add_book(entry_1, entry_2, rental_date_calendar, entry_4, genre_combobox, entry_5, window, librarian_id, book_data[6]),
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
        239.0,
        anchor="nw",
        text="Title:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        295.0,
        anchor="nw",
        text="Author:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        404.0,
        anchor="nw",
        text="Publisher:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        143.0,
        515.0,
        anchor="nw",
        text="Price:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        458.0,
        anchor="nw",
        text="Genre:",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        145.0,
        349.0,
        anchor="nw",
        text="Release date: ",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        341.0,
        148.0,
        anchor="nw",
        text="Add new item",
        fill="#000000",
        font=("Inter Black", 32 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: book_search(window, entry_1, mycursor, librarian_id),
        relief="flat"
    )
    button_3.place(
        x=132.0,
        y=140.0,
        width=60.0,
        height=60.0
    )

    window.resizable(False, False)
    window.mainloop()
