import os
from dotenv import load_dotenv

load_dotenv()

LOGIN_EMAIL = os.getenv("LOGIN_USER_1_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_USER_1_PASSWORD")
WRONG_PASSWORD = os.getenv("Invalid_Password")
