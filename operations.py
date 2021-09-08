from classes import Project, Fund, User
from validators import valid_date, valid_id, valid_number, matches, valid_input
from datetime import datetime
from tabulate import tabulate
import json


def prompt_project(database, user, isEdit=False):

    message = 'Enter new ' if isEdit else 'Enter '
    while True:
        title = valid_input(message + 'project title: ', isEdit).capitalize()
        if (isEdit and not title) or not does_exist(database['projects'], Project(title=title)):
            break
    details = input(message + 'project description: ')
    target = valid_number(message + 'fund target for your project: ', isEdit)
    start = str(datetime.now().date())
    end = valid_date(
        message + 'end date of your campaign formatted as yyyy-mm-dd: ', isEdit)
    project = user.start_project(title, details, target, start, end)
    return project


def start_project(database, user):

    database['projects'].append(prompt_project(database, user))
    print('Project created successfully')
    print('------------------------------')


def get_project_by_id(database, project_id):
    # not effiect || sequential scan || Time complexity: O(n)
    # could be improved by using binary search if the data is always sorted || Time complexity: Log(n)
    # Sorting by (User: email, Project:  )
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


def edit(database, user, project):
    print("leave field empty if you don't want to change a certain field")
    project.edit(prompt_project(database, user, True))


def delete(database, project):
    database['projects'].remove(project)
    print("Project deleted successfully")
    print("-------------------------------------")


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


def does_exist(records, obj):
    for record in records:
        if matches(record, obj):
            return True
    return False
