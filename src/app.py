import customtkinter as ctk
import imaplib
from tkinter.messagebox import showerror
from tkinter.font import Font
from PIL import ImageFont

current_user = None

def test(email_input, password_input):
    email_address = email_input.get()
    password = password_input.get()
    
    try:
        SMTP_SERVER = 'imap.gmail.com'
        SMTP_PORT = 993

        mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
        mail.login(email_address, password)

        current_user = {
            "email": email_address
        }
        
        print(mail)
        print("CURRENT USER: ", current_user)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        showerror("Login failed.", "Invalid email or password. Please check your credentials and try again.")
        return None
    
    finally:
        email_input.delete(0, "end")
        password_input.delete(0, "end")
    

def create_app():
    app = ctk.CTk()
    # custom_font = Font(file="src/Roboto-Medium.ttf", size=26)
    def show_help():
        help_popup = ctk.CTkToplevel(app)
        help_popup.title("Help")
        help_popup.resizable(False, False)
        help_popup.attributes("-topmost", True)
        help_popup.grab_set()

        ctk.CTkLabel(help_popup, text="WELCOME TO MYSCOREASSISTANT!", font=("Arial", 34)).pack()
        ctk.CTkLabel(help_popup, text="MyScoreAssistant is a simple and intuitive tool designed to help university students\n \
                     keep track of their exam grades effortlessly. The application automatically scans your university email\n \
                     for specific messages containing your exam scores, extracts the relevant details, and stores them in\n \
                     a secure database. With MyScoreAssistant, you can organize your academic progress seamlessly without\n \
                     having to manually search for or record your grades.", font=("Arial", 20), justify='left').pack(pady=30)

    custom_font = ImageFont.truetype(r"src\Roboto-Bold.ttf", size=30).font.family

    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=0) 
    app.grid_rowconfigure(2, weight=1) 
    app.grid_columnconfigure(0, weight=1)

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app.title("MyScoreAssistant")
    app.geometry(f"{screen_width}x{screen_height}+0+0")

    login_frame = ctk.CTkFrame(app, width=screen_width // 2, height= screen_height // 3)
    for i in range(8):
        login_frame.grid_rowconfigure(i, weight=1)
    login_frame.grid_columnconfigure(0, weight=1)

    login_frame.grid_propagate(False)
    login_frame.grid(row=1, column=0)

    email_input = ctk.CTkEntry(login_frame, placeholder_text="your-email@example.com", font=("Arial", 26))
    email_input.configure(width=500, height=60)
    email_input.grid(row=1, column=0)

    password_input = ctk.CTkEntry(login_frame, placeholder_text="Password", font=("Arial", 26), show="*")
    password_input.configure(width=500, height=60)
    password_input.grid(row=3, column=0)

    scrape_btn = ctk.CTkButton(login_frame, text="Login", font=("Arial", 30), command=lambda : test(email_input, password_input))
    scrape_btn.grid(row=6, column=0)

    help_button = ctk.CTkButton(app, text="Help", command=show_help, width=80, height=30)
    help_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

    return app