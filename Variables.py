from datetime import datetime

login_user_1_email = "madhukumarhm123.com@gmail.com"
password_user_1 = "Madhu@1234"
invalid_password = "1234567890"

first_name = "Madhu"
last_name = "Kumar"
telephone = "1234567890"
subscribe = "Yes"
password = "Password@123"

def generate_email():  # Fixed spelling of 'generate'
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "madhu" + time_stamp + "@gmail.com"  # Corrected the spelling of 'gmail'
