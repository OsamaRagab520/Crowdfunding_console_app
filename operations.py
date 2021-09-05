from classes import Project, Fund, User
from validators import valid_date, valid_id, valid_number
from datetime import datetime
from tabulate import tabulate
import json


def start_project(database, user):
    try:
        title = input('Enter your project title: ').strip().capitalize()
        details = input('Descripe your project: ')
        target = valid_number('How much you want to raise for your project: ')
        start = str(datetime.now().date())
        end = valid_date(
            'Enter end date of  your campaign formatted as yyyy-mm-dd: ')
        project = user.start_project(title, details, target, start, end)
        database['projects'].append(project)
        print('Project created successfully')
        print('------------------------------')
    except Exception as e:
        print(f'Something went wrong, error type: {e}')


def get_project_by_id(database, project_id):
    # not effiect || sequential scan || Time complexity: O(n)
    # could be improved by using binary search if the data is always sorted || Time complexity: Log(n)
    # Sorting by (User: email, Project: id)
    for project in database['projects']:
        if project.id == project_id:
            return project


def view(database, user=None):
    projects = []
    if user:
        projects = [[project.id, project.title, project.target]
                    for project in database['projects'] if user.is_project_author(project)]

    else:
        funds = database['funds']
        projects = [[project.id, project.title, f'{project.total_funds(funds)}/{project.target}']
                    for project in database['projects']]
    print()
    print(tabulate(projects, headers=[
        'Project_id', 'Project Title', 'Project target fund'], tablefmt='orgtbl', stralign="right"))
    print()
    project_id = valid_id(
        'Type project id that you are interested in: ', [project[0] for project in projects])
    return get_project_by_id(database, project_id)


def fund(database, project, user):
    amount = valid_number(
        f'Enter the amount of money you wanna fund {project.title}: ')
    fund = user.fund_project(project.id, amount)
    database['funds'].append(fund)


def load(filename='data.txt'):
    database = {'users': [], 'projects': [], 'funds': []}

    try:
        with open(filename) as f:
            data = json.load(f)
            for key, obj in zip(data.keys(), (User, Project, Fund)):
                database[key] = [obj(**attrs) for attrs in data[key]]

            return database

    except FileNotFoundError:
        print('File doesn\'t not exist\ninitializing empty database')
        return database

        # for explanation in project preview

        # database = {'users': [], 'projects': [], 'funds': []}
        # database['users'] = [User(**user) for user in data['users']]
        # database['projects'] = [Project(**project)
        #                         for project in data['projects']]
        # database['funds'] = [Fund(**fund) for fund in data['funds']]


def save(database, filename='data.txt'):
    with open(filename, 'w') as f:

        for key in database.keys():
            database[key] = list(map(vars, database[key]))
        json.dump(database, f, indent=4)
