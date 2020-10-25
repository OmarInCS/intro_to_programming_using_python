
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def get_course_name(self):
        return self.__course_name

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        for s in self.__students:
            if s.name == name:
                self.__students.remove(s)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def __repr__(self):
        return f"Course: {self.__course_name}, Students: {self.__students}"
