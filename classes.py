from datetime import datetime
from validators import valid_date


class User:
    id = 0

    def __init__(self, fname=None, lname=None, email=None, password=None, phone=None, id=None):
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

    def __init__(self, user_id=None, title=None, details=None, target=None, start=None, end=None, id=None):
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

    def edit(self, project):
        project.id = self.id
        for attr, value in vars(project).items():
            if value:
                setattr(self, attr, value)

    def total_funds(self, funds):
        return int(sum([fund.amount for fund in funds if self.id == fund.project_id]))


class Fund:
    id = 0

    def __init__(self, user_id=None, project_id=None, amount=None, id=None):
        self.user_id = user_id
        self.project_id = project_id
        self.amount = amount
        self.id = id if id else Fund.id
        Fund.id = self.id + 1

    def __repr__(self):
        return f'Fund({self.user_id}, {self.project_id}, {self.amount})'
