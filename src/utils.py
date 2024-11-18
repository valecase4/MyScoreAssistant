from dotenv import load_dotenv
import os

def get_credentials():
    load_dotenv()
    app_password = os.getenv("APP_PASSWORD")

    return app_password