from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
import sqlite3
import mysql.connector


def generate_qr_codes(output_file):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="library"
    )
    cursor = db.cursor()

    cursor.execute("SELECT book_id, title, author FROM Books")
    books = cursor.fetchall()

    c = canvas.Canvas(output_file, pagesize=letter)
    c.setTitle("QR Codes")

    x = 50
    y = 750

    # Set QR code size
    qr_size = 100

    for book in books:
        book_id, title, author = book

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(f"{book_id}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        c.drawInlineImage(img, x, y - qr_size, qr_size, qr_size)
        text = title + ', ' + author
        c.drawString(x, y - qr_size - 20, text)
        y -= qr_size + 50
        if y <= 50:
            c.showPage()
            y = 750

    c.save()
    db.close()
