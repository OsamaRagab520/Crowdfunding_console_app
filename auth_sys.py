from enum import unique
from classes import User
from validators import valid_email, valid_input, valid_password, valid_phone
from operations import does_exist


def register(database):
    # email not in [user.email for user in database['users']]
    fname = valid_input("Enter your first name: ")
    lname = valid_input("Enter your last name: ")
    while True:
        email = valid_email()
        # if does_exist(database['users'],'email', value)
        if not does_exist(database['users'], User(email=email)):
            break
        print("This email is already registered")
    # hasing the password
    password = valid_password()
    phone = valid_phone(database)
    user = User(fname, lname, email, password, phone)
    database['users'].append(user)
    return user


def login(database, email=None):
    email = valid_email("Enter your Email: ") if not email else email
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
