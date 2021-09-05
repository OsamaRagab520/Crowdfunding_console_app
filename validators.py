from datetime import datetime, date
import re


def valid_input(message):
    # Prompet
    data = None
    while not data:
        data = input(message).strip()
    return data


def valid_number(message):
    while True:
        try:
            value = float(input(message))
            return value
        except:
            print('Enter a valid amount of money example 300')


# bad design
def valid_command(message, commands_string):
    while True:
        c = input(message).strip().lower()
        if c in list(commands_string+'q'):
            return c
        else:
            print('Invalid command')


def valid_id(message, id_list):
    while True:
        try:
            id = int(input(message).strip().lower())
            if id in id_list:
                return id
        except ValueError:
            pass
        print('Invalid Id')


def valid_date(message, allow_empty=False):
    while True:
        if allow_empty:
            end_date = input(message).strip().lower()
            if not end_date:
                return None
        else:
            end_date = valid_input(message)
        try:
            if date.fromisoformat(end_date) > datetime.now().date():
                return end_date
            else:
                print('the date must be in the future')
        except ValueError:
            print('Bad date format example: 2021-05-01')
            end_date = valid_input(message)


def valid_email(database, message="Enter your Email: ", reg=False):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        email = valid_input(message)
        if reg:
            if re.fullmatch(email_pattern, email) and email not in [user.email for user in database['users']]:
                return email
            else:
                print('Invalid Email or already taken')
        else:
            if re.fullmatch(email_pattern, email):
                return email
            else:
                print('Invalid Email')


def valid_password(message="Enter your password: "):
    while True:
        password = valid_input(message)
        if input('confirm password: ').strip() == password:
            return password
        else:
            print('Password mismatch')


def valid_phone(database, message="Enter your phone: "):

    def verify_phone(phone):
        if phone.isnumeric() and phone[:2] == '01' and len(phone) == 11 and phone not in [user.phone for user in database['users']]:
            return True
        else:
            False

    while True:
        phone = valid_input(message)
        if verify_phone(phone):
            return phone
        else:
            print('Invalid phone or already taken')
