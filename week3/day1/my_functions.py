
def get_bmi(weight, height):
    return weight / (height / 100) ** 2


def get_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_percent(m=25, fm=25):
    return m / fm * 100


def get_grade(pct):
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
