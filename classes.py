from datetime import datetime
from validators import valid_date


class User:
    id = 0

    def __init__(self, fname, lname, email, password, phone, id=None):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phone = phone
        self.id = id if id else User.id
        User.id = self.id + 1

    def __repr__(self):
        return f'User({self.fname}, {self.lname}, {self.email}, {self.password}, {self.phone}, {self.id})'

    def start_project(self, title, details, target, start, end):
        return Project(self.id, title, details, target, start, end)

    def fund_project(self, project_id, amount):
        return Fund(self.id, project_id, amount)

    def is_project_author(self, project):
        if project.user_id == self.id:
            return True
        else:
            return False


class Project:
    id = 0

    def __init__(self, user_id, title, details, target, start, end, id=None):
        self.user_id = user_id
        self.title = title
        self.details = details
        self.target = target
        self.start = start
        self.end = end
        self.id = id if id else Project.id
        Project.id = self.id + 1

    def __repr__(self):
        return f'Project({self.user_id}, {self.title}, {self.details}, {self.target}, {self.start}, {self.end})'

    def edit(self):
        print("leave field empty if you don't want to change a certain field")
        # handle bad inputs
        title = input('Enter your new project title: ').strip().capitalize()
        self.title = self.title if not title else title
        details = input('Enter your new project description: ')
        self.details = self.details if not details else details
        target = input('Enter your new fund target for your project: ')
        self.target = self.target if not target else target
        end = valid_date(
            'Enter your new end date of  your campaign formatted as yyyy-mm-dd: ', True)
        self.end = self.target if not end else end

    def total_funds(self, funds):
        return int(sum([fund.amount for fund in funds if self.id == fund.project_id]))


class Fund:
    id = 0

    def __init__(self, user_id, project_id, amount, id=None):
        self.user_id = user_id
        self.project_id = project_id
        self.amount = amount
        self.id = id if id else Fund.id
        Fund.id = self.id + 1

    def __repr__(self):
        return f'Fund({self.user_id}, {self.project_id}, {self.amount})'
