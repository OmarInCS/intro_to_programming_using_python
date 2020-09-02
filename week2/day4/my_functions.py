
def get_bmi(weight, height):
    return weight / height ** 2


def get_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_pct(m=5, fm=15):
    return m / fm * 100