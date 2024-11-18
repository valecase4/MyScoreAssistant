import imaplib
import email
from email.header import decode_header

from .utils import get_credentials

def get_mail_client(email_address):
    SMTP_SERVER = 'imap.gmail.com'
    SMTP_PORT = 993

    password = get_credentials()

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(email_address, password)
    
    return mail

def get_last_email(email_address):
    SMTP_MAILBOX = "INBOX"
    SUBJECT_FILTER = "Pubblicazione Voto Appello"
    FROM_FILTER = "webhelp@unimore.it"

    mail = get_mail_client(email_address)
    mail.select(SMTP_MAILBOX)

    try:
        search_criteria = f'(FROM "{FROM_FILTER}" SUBJECT "{SUBJECT_FILTER}")'
        status, messages = mail.search(None, search_criteria)

        if status != "OK":
            print("No messages found!")

            return None
        
        email_ids = messages[0].split()

        if not email_ids:
            print("No matching emails found.")

        latest_email_id = email_ids[-1]
        status, data = mail.fetch(latest_email_id, "(RFC822)")

        if status != "OK":
            print("Failed to fetch the email")
            return None
        
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Decode the email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            # If it's a byte, decode it to a string
            subject = subject.decode(encoding if encoding else "utf-8")

        # Get the sender
        from_ = msg.get("From")

        # Extract the email body
        body = None
        if msg.is_multipart():
            for part in msg.walk():
                # If the part is text/plain or text/html
                if part.get_content_type() in ("text/plain", "text/html"):
                    body = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8")
                    break
        else:
            # For non-multipart emails
            body = msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8")

        # Return the parsed email details
        return body

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        mail.logout()