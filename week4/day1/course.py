
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def get_course_name(self):
        return self.__course_name

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def __gt__(self, other):
        return self.get_nb_of_students() > other.get_nb_of_students()

    def __add__(self, other):
        self.__students.append(other)

    def __repr__(self):
        return f"Course: {self.__course_name}, {self.__students}"