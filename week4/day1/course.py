
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)

    def get_course_name(self):
        return self.__course_name


if __name__ == "__main__":
    c1 = Course("Python")
    c2 = Course("Java")

    c1.add_student("Abdullah")
    c1.add_student("Essam")
    c1.add_student("Mohamed")
    c1.add_student("Omar")

    print(c1.get_students())
    print(c1.get_nb_of_students())

    c1.drop_student("Omar")

    print(c1.get_students())
    print(c1.get_nb_of_students())
