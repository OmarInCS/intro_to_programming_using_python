from week4.day1.student import Student


class Course:

    def __init__(self, course_name):
        self.__course_name = course_name
        self.__students = []

    def get_course_name(self):
        return self.__course_name

    def add_student(self, std):
        self.__students.append(std)

    def drop_student(self, name):
        for obj in self.__students:
            if obj.name == name:
                self.__students.remove(obj)

    def get_students(self):
        return self.__students

    def get_nb_of_students(self):
        return len(self.__students)


if __name__ == '__main__':
    c1 = Course("Python")
    c1.add_student(Student(101, "Ahmed", 500))
    c1.add_student(Student(102, "Mohamed", 500))
    c1.add_student(Student(103, "Omar", 500))
    c1.add_student(Student(104, "Saud", 500))
    print(c1.get_students())
    print(c1.get_nb_of_students())
    c1.drop_student("Omar")
    print(c1.get_students())
    print(c1.get_nb_of_students())