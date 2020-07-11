
class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def get_course_name(self):
        return self.__course_name

    def add_student(self, std_name):
        self.__students.append(std_name)

    def drop_student(self, std_name):
        self.__students.remove(std_name)

    def drop_student_by_index(self, idx):
        self.__students.pop(idx)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)


if __name__ == '__main__':
    c1 = Course("Java")
    print(c1.get_nb_of_students())
    c1.add_student("Walid")
    c1.add_student("Zaid")
    c1.add_student("Obaid")

    print(c1.get_nb_of_students())
    c1.drop_student("Walid")
    c1.drop_student_by_index(1)

    print(c1.get_students())

