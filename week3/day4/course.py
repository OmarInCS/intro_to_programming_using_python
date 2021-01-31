
class Course:

    def __init__(self, course_title):
        self.__course_title = course_title
        self.__students = []

    def get_course_title(self):
        return self.__course_title

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)
