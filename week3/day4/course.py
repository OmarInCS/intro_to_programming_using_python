
class Course:

    def __init__(self, title, dur):
        self.__title = title
        self.__students = []
        self.__duration = dur

    def get_title(self):
        return self.__title

    def get_students(self):
        return self.__students

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_nb_students(self):
        return len(self.__students)

    def __gt__(self, other):
        return self.get_nb_students() > other.get_nb_students() and self.__duration > other.__duration

    def __add__(self, other):
        self.__students.append(other)
