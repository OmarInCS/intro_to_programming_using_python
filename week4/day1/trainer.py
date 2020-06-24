from week4.day1.course import Course


class Trainer:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.courses = []

    def get_annual_salary(self):
        return self.salary * 12

    def add_course(self, course):
        self.courses.append(course)
        course.trainer = self

    def drop_course(self, title):
        for cour in self.courses:
            if cour.get_course_name() == title:
                self.courses.remove(cour)
                return


if __name__ == '__main__':
    c1 = Course("Java")
    c2 = Course("Python")
    c1.add_student("Ahmed")
    c1.add_student("Mohamed")
    c2.add_student("Hala")
    c2.add_student("Soumaiah")
    
    t1 = Trainer("Omar", 15000)
    t1.add_course(c1)
    t1.add_course(c2)
    t1.drop_course("Java")

    print()