
def get_pct(mark=25, final_mark=25):
    return mark / final_mark * 100


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

