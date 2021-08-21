
class Course:

    def __init__(self, title, price):
        self.__title = title
        self.__price = price
        self.__students = []

    def get_title(self):
        return self.__title

    def get_price(self):
        return  self.__price

    def get_students(self):
        return self.__students

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_nb_students(self):
        return len(self.__students)

    def __gt__(self, other):
        return self.__price > other.__price

    def __add__(self, name):
        self.__students.append(name)
        return self

