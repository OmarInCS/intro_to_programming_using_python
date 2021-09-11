
class Student:

    full_mark = 25

    def __init__(self, name, mark):
        self.__name = name
        self.__mark = mark

    def get_name(self):
        return self.__name

    def set_mark(self, value):
        if value >= 0:
            self.__mark = value

    def get_mark(self):
        return self.__mark

    def calc_pct(self):
        return self.__mark / Student.full_mark * 100

    def find_grade(self):
        pct = self.calc_pct()
        if pct >= 50:
            return "Pass"
        else:
            return "Fail"
