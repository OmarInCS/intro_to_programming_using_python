
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def get_course_name(self):
        return self.__course_name

    def add_student(self, student):
        self.__students.append(student)
        student.course = self

    def drop_student(self, name):
        for std in self.__students:
            if std.name == name:
                self.__students.remove(std)
                return

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def __repr__(self):
        return f"Course: {self.__course_name}"