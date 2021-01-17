
class Patient:

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def get_bmi(self):
        return self.weight / self.height ** 2

    def get_status(self):
        bmi = self.get_bmi()
        if bmi < 18.5: return "Underweight"
        elif bmi < 25: return "Normal"
        elif bmi < 30: return "Overweight"
        else: return "Obese"