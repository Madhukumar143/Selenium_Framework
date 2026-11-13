from datetime import datetime



first_name = "Madhu"
last_name = "Kumar"
telephone = "1234567890"
subscribe = "Yes"
password = "Password@123"

def generate_email():  # Fixed spelling of 'generate'
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "madhu" + time_stamp + "@gmail.com"
