
def get_bmi(weight, height):
    return weight / height ** 2


def get_status(weight=70, height=1.7):
    bmi = get_bmi(weight, height)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
