# MODULES #
from pathlib import Path
from tkinter import Tk, Canvas, Listbox, Scrollbar, PhotoImage, Toplevel, Button
import addbook
import bookoverview_5


# PATHS
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\wikto\OneDrive\Pulpit\Bazy-Danych\DB Project\Assets\BookSearch")


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


def back_raport_page(window, librarian_id):
    window.destroy()

    new_window = Tk()
    new_window.title("Dodawanie nowego wypożyczenia - eAGH")
    new_window.geometry("1000x800")

    tablica = ["", "", "", "", "", "", ""]

    addbook.show_add_book_page(new_window, librarian_id, tablica)


def show_search_page(window, librarian_id, result):
    align_window(window)

    def on_select(event):
        index = listbox.curselection()

        window.destroy()

        new_window = Tk()
        new_window.title("Przeglad książki - eAGH")
        new_window.geometry("1000x800")

        bookoverview_5.show_book_overview(new_window, result[index[0]][2], result, librarian_id)

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

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))

    image_1 = canvas.create_image(
        851.0,
        161.0,
        image=image_image_1
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_raport_page(window, librarian_id),
        relief="flat"
    )
    button_2.place(
        x=400.0,
        y=693.0,
        width=184.0,
        height=47.0
    )

    canvas.create_text(
        352.0,
        139.0,
        anchor="nw",
        text="Wyniki wyszukiwania",
        fill="#A71930",
        font=("Inter ExtraBold", 30 * -1)
    )

    scrollbar = Scrollbar(window)
    scrollbar.pack(side='right', fill='y')

    listbox = Listbox(
        window,
        bg="#EBEBEB",
        bd=0,
        highlightthickness=0,
        relief="ridge",
        font=("Inter Black", 18),
        yscrollcommand=scrollbar.set
    )

    i = 1

    for item in result:
        listbox.insert('end', f"{i}. " + item[0] + ", " + item[1])
        i += 1

    listbox.place(x=150, y=200, width=700, height=480)
    scrollbar.config(command=listbox.yview)

    listbox.bind('<<ListboxSelect>>', on_select)

    window.resizable(False, False)
    window.mainloop()
