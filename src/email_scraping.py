import imaplib
import email
from utils import get_credentials

def get_mail_client(email_address, password_file):
    SMTP_SERVER = 'imap.gmail.com'
    SMTP_PORT = 993

    password = get_credentials()

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(email_address, password)
    return mail

