from classes import User
from validators import valid_email, valid_input, valid_password, valid_phone


def register(database):
    fname = valid_input("Enter your first name: ")
    lname = valid_input("Enter your last name: ")
    email = valid_email(database)
    # hasing the password
    password = valid_password()
    phone = valid_phone(database)
    user = User(fname, lname, email, password, phone)
    database['users'].append(user)
    return user


def login(database, email=None):
    if not email:
        email = valid_email("Enter your Email: ")
    password = input("Enter your password: ").strip()

    for user in database['users']:
        # check with the hashed password
        if user.email == email:
            if user.password == password:
                return user
            else:
                print('Wrong password')
                login(database, email)
        else:
            return None
