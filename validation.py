from datetime import datetime

def get_non_empty_input(message):
    while True:
        value = input(message)

        if value.strip() != "":
            return value
        else:
            print("This field cannot be empty. Please try again.")

def get_date_input(message):
    while True:
        date = input(message)

        try:
            datetime.strptime(date, "%d/%m/%Y")
            return date
        except ValueError:
            print("Please enter the date in DD/MM/YYYY format.")