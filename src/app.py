import customtkinter as ctk

def create_app():
    app = ctk.CTk()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app.title("MyScoreAssistant")
    app.geometry("400x400")

    return app