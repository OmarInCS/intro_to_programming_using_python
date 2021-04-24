
class Course:

    def __init__(self, title):
        self.__title = title
        self.__students = []

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def get_title(self):
        return self.__title

    def __gt__(self, other):
        return self.get_nb_of_students() > other.get_nb_of_students()

    def __iadd__(self, other):
        self.__students.append(other)
        return self

    def __repr__(self):
        return f"Course: {self.__title}"