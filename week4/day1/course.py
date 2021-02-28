
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def add_student(self, std_name):
        self.__students.append(std_name)

    def drop_student(self, std_name):
        self.__students.remove(std_name)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def get_course_name(self):
        return self.__course_name

    def __gt__(self, other):
        return self.get_nb_of_students() > other.get_nb_of_students()

    def __add__(self, other):
        self.add_student(other)

    def __repr__(self):
        return f"#students: {self.get_nb_of_students()}, {self.__students}"