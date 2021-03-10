
class Course:

    def __init__(self, title):
        self.__course_title = title
        self.__stduents = []

    def get_course_title(self):
        return self.__course_title

    def add_student(self, name):
        self.__stduents.append(name)

    def drop_student(self, name):
        self.__stduents.remove(name)

    def get_students(self):
        return self.__stduents

    def get_nb_of_students(self):
        return len(self.__stduents)

    def __gt__(self, other):
        return self.get_nb_of_students() > other.get_nb_of_students()

    def __add__(self, other):
        self.__stduents.append(other)

    def __repr__(self):
        # return "Course: " + self.__course_title + " "
        return f"Course: {self.__course_title}, {self.__stduents}"
