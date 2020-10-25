
class Student:

    final_mark = 25     # static variable

    def __init__(self, name, mark):
        self.name = name    # instance variable
        self.__mark = mark    # instance variable

    def set_mark(self, value):
        if value > 0 and value < Student.final_mark:
            self.__mark = value

    def get_mark(self):
        return self.__mark

    def get_pct(self):
        return self.__mark / Student.final_mark * 100

    def get_grade(self):
        pct = self.get_pct()
        if pct > 85:
            return "Excellent"
        elif pct > 75:
            return "V. Good"
        elif pct > 65:
            return "Good"
        elif pct >= 50:
            return "Pass"
        else:
            return "Fail"

    def __repr__(self):
        return f"Name: {self.name}, {self.__mark}"
