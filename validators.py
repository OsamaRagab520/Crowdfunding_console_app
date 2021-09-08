from datetime import datetime, date
import re


def valid_input(message, allow_empty=False):
    # Prompet
    data = input(message).strip()
    while not data and not allow_empty:
        print('Empty string is not allowed')
        data = input(message).strip()
    return data


def valid_number(message, allow_empty=False):
    while True:
        value = None
        try:
            value = float(input(message))
            if value > 0:
                return value
            else:
                print("Must be greater than 0")
        except:
            if allow_empty and not value:
                return value
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
        end_date = input(message).strip()
        if allow_empty:
            if not end_date:
                return None
        try:
            if date.fromisoformat(end_date) > datetime.now().date():
                return end_date
            else:
                print('the date must be in the future')
        except ValueError:
            print('Bad date format example: 2021-05-01')


def valid_email(message="Enter your Email: "):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        email = input(message).strip()
        vaild = re.fullmatch(email_pattern, email)
        if vaild:
            return email
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


def matches(ref_obj, obj):
    # handling empty obj
    if type(ref_obj) != type(obj):
        raise ValueError
    for attr, value in vars(obj).items():
        if value is not None and attr != 'id' and value != getattr(ref_obj, attr):
            return False

    return True
