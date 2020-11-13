
class Student:

    final_mark = 25

    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark

    def set_mark(self, value):
        if value >= 0 and value <= Student.final_mark:
            self.__mark = value

    def get_mark(self):
        return self.__mark

    def get_percentage(self):
        return self.__mark / Student.final_mark * 100

    def get_grade(self):
       pct = self.get_percentage()
       if pct > 85:
           return "Excellent"
       elif pct > 75:
           return "V. Good"
       elif pct > 65:
           return "good"
       elif pct >= 50:
           return "Pass"
       else:
           return "Fail"
