from auth_sys import register, login
from validators import valid_command
from operations import start_project, view, fund, load, save

database = load()


def start_app():
    welcome = 'Welcome to my Crowd-Funding APP\nLogin: l\nRegister: r\nQuit: q\nType one of the commands: '
    command = valid_command(welcome, 'lr')
    user = None

    if command == 'l':
        user = login(database)
    elif command == 'r':
        user = register(database)
    else:
        exit(0)

    program_loop(user)


def program_loop(user):
    while True:
        if user:
            print('Enter one of the Commands')
            op = valid_command(
                'Start Project: s, View Active Projects: v, Edit your Projects: e, Delete one of your project: d, Quit: q: ', 'sved')
            if op == 's':
                start_project(database, user)
            elif op == 'e':
                view(database, user).edit()
            elif op == 'd':
                database['projects'].remove(view(database, user))
            elif op == 'v':
                project = view(database)
                f = valid_command(
                    f'Do you want to fund {project.title} y/n? ', 'yn')
                if f == 'y':
                    fund(database, project, user)
            else:
                save(database)
                exit(0)

        else:
            c = valid_command(
                'You not registered in our database, do you want to register? enter y\nlogin again: l\nQuit: q\nCommand:  ', 'yl')
            if c == 'y':
                user = register(database)
            elif c == 'l':
                user = login(database)
            else:
                save(database)
                exit(0)


start_app()
