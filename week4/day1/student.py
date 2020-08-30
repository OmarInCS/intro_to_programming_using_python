

class Student:

    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def __repr__(self):
        return self.name