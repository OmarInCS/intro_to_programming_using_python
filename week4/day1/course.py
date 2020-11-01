
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def get_course_name(self):
        return self.__course_name

    def add_student(self, student):
        self.__students.append(student)

    def drop_student(self, student):
        self.__students.remove(student)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def __add__(self, other):
        self.__students.append(other)

    def __gt__(self, other):
        return len(self.__students) > len(other.__students)

    def __repr__(self):
        return str(self.__students)
