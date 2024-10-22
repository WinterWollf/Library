# MODULES #
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# user_data = ["Test", "Test"]
# book_data = ["Test", "Test"]
# status = 1


def send_email(status, user_data, book_data, return_date=None, day_after=0):
    # Dane do logowania do konta Interia
    sender_email = ""
    sender_password = ""

    # Adres odbiorcy
    receiver_email = ""
    receiver_email_2 = ""

    # Treść wiadomości
    if status == 0:
        if day_after <= 0:
            subject = "Potwierdzenie zwrotu"
            message = f"Cześć {user_data[0]} {user_data[1]}. Potwierdzamy pomyślny zwrotu książki pt. {book_data[0]}, {book_data[1]}. Do zobaczenie wkrótce!"
        else:
            subject = "Potwierdzenie zwrotu"
            message = f"Cześć {user_data[0]} {user_data[1]}. Potwierdzamy pomyślny zwrotu książki pt. {book_data[0]}, {book_data[1]}. Książka została zwrócona {day_after} dni po terminie! Przy kolejnej wizycie proszę zgłosić się do bibliotekarza."
    else:
        subject = "Potwierdzenie wypożyczenia"
        message = f"Cześć {user_data[0]} {user_data[1]}. Potwierdzamy pomyślne wypożyczenie książki pt. {book_data[0]}, {book_data[1]}. Książkę należy zwróci do {return_date}. Miłej lektury!"

    # Tworzenie wiadomości
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Tworzenie wiadomości 2
    msg_2 = MIMEMultipart()
    msg_2['From'] = sender_email
    msg_2['To'] = receiver_email_2
    msg_2['Subject'] = subject

    # Dodanie treści wiadomości
    html = """\
    <html>
      <body>
        <p>{}<br>
           <table cellpadding="0" cellspacing="0" border="0" globalstyles="[object Object]" class="table__StyledTable-sc-1avdl6r-0 iBAlEo" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;"><tbody><tr><td><table cellpadding="0" cellspacing="0" border="0" globalstyles="[object Object]" class="table__StyledTable-sc-1avdl6r-0 iBAlEo" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;"><tbody><tr><td style="vertical-align: top;"><table cellpadding="0" cellspacing="0" border="0" globalstyles="[object Object]" class="table__StyledTable-sc-1avdl6r-0 iBAlEo" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;"><tbody><tr><td height="30"></td></tr><tr><td style="text-align: center;"><table cellpadding="0" cellspacing="0" border="0" globalstyles="[object Object]" class="table__StyledTable-sc-1avdl6r-0 iBAlEo" style="display: inline-block; vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;"><tbody><tr style="text-align: center;"><td><a href="https://www.facebook.com/AGH.Krakow/?locale=pl_PL" color="#7075db" class="social-links__LinkAnchor-sc-py8uhj-2 kKbTXZ" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/facebook-icon-2x.png" alt="facebook" color="#7075db" width="24" class="social-links__LinkImage-sc-py8uhj-1 ijDZrg" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;"></a></td><td width="5"><div></div></td><td><a href="https://x.com/AGH_Krakow" color="#7075db" class="social-links__LinkAnchor-sc-py8uhj-2 kKbTXZ" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/twitter-icon-2x.png" alt="twitter" color="#7075db" width="24" class="social-links__LinkImage-sc-py8uhj-1 ijDZrg" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;"></a></td><td width="5"><div></div></td><td><a href="https://www.linkedin.com/school/agh-university-of-krakow/?originalSubdomain=pl" color="#7075db" class="social-links__LinkAnchor-sc-py8uhj-2 kKbTXZ" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/linkedin-icon-2x.png" alt="linkedin" color="#7075db" width="24" class="social-links__LinkImage-sc-py8uhj-1 ijDZrg" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;"></a></td><td width="5"><div></div></td><td><a href="https://www.instagram.com/agh.krakow/" color="#7075db" class="social-links__LinkAnchor-sc-py8uhj-2 kKbTXZ" style="display: inline-block; padding: 0px; background-color: rgb(112, 117, 219);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/instagram-icon-2x.png" alt="instagram" color="#7075db" width="24" class="social-links__LinkImage-sc-py8uhj-1 ijDZrg" style="background-color: rgb(112, 117, 219); max-width: 135px; display: block;"></a></td><td width="5"><div></div></td></tr></tbody></table></td></tr></tbody></table></td><td width="46"><div></div></td><td style="padding: 0px; vertical-align: middle;"><h2 color="#000000" class="name__NameContainer-sc-1m457h3-0 fTuwKP" style="margin: 0px; font-size: 18px; color: rgb(0, 0, 0); font-weight: 600;"><span>e-AGH</span><span>&nbsp;</span><span></span></h2><p color="#000000" font-size="medium" class="job-title__Container-sc-1hmtp73-0 dNrmoE" style="margin: 0px; color: rgb(0, 0, 0); font-size: 14px; line-height: 22px;"><span>Elektroniczny System Biblioteczny</span></p><p color="#000000" font-size="medium" class="company-details__CompanyContainer-sc-j5pyy8-0 lkZFXS" style="margin: 0px; font-weight: 500; color: rgb(0, 0, 0); font-size: 14px; line-height: 22px;"><span>AGH im. Stanisława Staszica w Krakowie</span></p><p color="#000000" font-size="medium" class="custom-field__CustomFieldContainer-sc-190n2f-0 dgFmdR" style="color: rgb(0, 0, 0); margin: 0px; font-size: 14px; line-height: 22px;"><span>Bazy Danych - Wiktor Szyszka</span></p><table cellpadding="0" cellspacing="0" border="0" globalstyles="[object Object]" class="table__StyledTable-sc-1avdl6r-0 iBAlEo" style="width: 100%; vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;"><tbody><tr><td height="30"></td></tr><tr><td color="#f86295" direction="horizontal" width="auto" height="1" class="color-divider__Divider-sc-1h38qjv-0 CxZvS" style="width: 100%; border-bottom: 1px solid rgb(167, 25, 48); border-left: none; display: block;"></td></tr><tr><td height="30"></td></tr></tbody></table><table cellpadding="0" cellspacing="0" border="0" globalstyles="[object Object]" class="table__StyledTable-sc-1avdl6r-0 iBAlEo" style="vertical-align: -webkit-baseline-middle; font-size: medium; font-family: Arial;"><tbody><tr><td height="30"></td></tr></tbody></table><a textcolor="#000000" href="https://www.hubspot.com/email-signature-generator?utm_source=create-signature" target="_blank" rel="noopener noreferrer" class="viral-link__Anchor-sc-1kv0kjx-0 eQMwVs" style="font-size: 12px; display: block; color: rgb(0, 0, 0);"></a></td></tr></tbody></table></td></tr></tbody></table>
        </p>
      </body>
    </html>
    """.format(message)
    msg.attach(MIMEText(html, 'html'))
    msg_2.attach(MIMEText(html, 'html'))

    # Utworzenie połączenia z serwerem SMTP Interia
    server = smtplib.SMTP('poczta.interia.pl', 587)
    server.starttls()

    # Logowanie do konta
    server.login(sender_email, sender_password)

    # Wysłanie wiadomości
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.sendmail(sender_email, receiver_email_2, msg_2.as_string())

    # Zamknięcie połączenia
    server.quit()

    print("DZIALA")
