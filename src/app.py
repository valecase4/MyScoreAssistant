import customtkinter as ctk
from .email_scraping import get_mail_client
from .email_scraping import get_last_email
from .utils import parse_email_body
from .db import add_exam_to_db, create_table

def test():
    text = get_last_email("310481@studenti.unimore.it")
    
    text = parse_email_body(text)
    create_table()

    add_exam_to_db(id='1', name=text["exam_name"], score=text["score"], date=text["exam_date"])
    

def create_app():
    app = ctk.CTk()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app.title("MyScoreAssistant")
    app.geometry("400x400")

    scrape_btn = ctk.CTkButton(app, text="Test Email", command=test)
    scrape_btn.pack()

    return app