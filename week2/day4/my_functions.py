
def get_pct(mark=25, final_mark=25):
    return mark / final_mark * 100


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


def calc_bmi(weight, height):
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
