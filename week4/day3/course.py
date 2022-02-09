
class Course:

    def __init__(self, title, price):
        self.__title = title
        self.__price = price
        self.__students = []

    def add_student(self, name):
        self.__students.append(name)

    def drop_student(self, name):
        self.__students.remove(name)

    def get_nb_students(self):
        return len(self.__students)

    def get_students(self):
        return self.__students

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    @property
    def price(self):
        return self.__price

    def set_price(self, value):
        if value >= 200 and value <= 3000:
            self.__price = value
        else:
            print("Invalid Price")

    @price.setter
    def price(self, value):
        if value >= 200 and value <= 3000:
            self.__price = value
        else:
            print("Invalid Price")

    def __gt__(self, other):
        return self.__price > other.__price

    def __iadd__(self, other):
        self.__students.append(other)
        return self


print(__name__)
if __name__ == "__main__":
    c1 = Course("Java", 1000)
    c2 = Course("Python", 1200)

    c1.add_student("Ali")
    c1.add_student("Wael")
    c1.add_student("Fahad")
    c1 += "Adel"

    print(c1.get_nb_students())
    print(c1.get_students())

    c1.drop_student("Wael")
    print(c1.get_nb_students())
    print(c1.get_students())

    print(c1 > c2)
