
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
        self.__students.append(other)

    def __str__(self):
        return f"Course {self.__title}: {self.__price}, {self.__students}"


if __name__ == "__main__":
    c1 = Course("Java", 1200)
    c1.add_student("Ahmed")
    c1.add_student("Wael")
    c1.add_student("Ali")

    print(c1.get_students())
    print(c1.get_nb_students())

    c1.drop_student("Wael")
    print(c1.get_students())
    print(c1.get_nb_students())

    c2 = Course("SQL", 1000)
    c2.add_student("Wael")
    c2 + "Yousef"

    print(c2.get_students())
    print(c2.get_nb_students())

    print(c1 > c2)