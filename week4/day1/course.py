
class Course:

    def __init__(self, title, price):
        self.__title = title
        self.__price = price
        self.__students = []

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_students(self):
        return self.__students

    def get_nb_students(self):
        return len(self.__students)

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def __gt__(self, other):
        return self.__price > other.__price

    def __add__(self, other):
        self.add_student(other)
        return self

    def __repr__(self):
        return f"Course: {self.__title}, {self.__students}"


if __name__ == "__main__":
    print(__name__)
    c1 = Course("Java", 1000)
    c1.add_student("Khalid")
    c1.add_student("Ali")
    c1.add_student("Ahmed")

    print(c1.get_students())
    print(c1.get_nb_students())

    c1.drop_student("Ali")
    print(c1.get_students())
    print(c1.get_nb_students())

    c2 = Course("Python", 1200)
    c2 += "Wael"
    c2 += "Yasser"
    print(c2.get_students())

    print(c1 > c2)
    print(c1)