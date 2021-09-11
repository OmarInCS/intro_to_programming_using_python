
def get_bmi(weight, height):
    return weight / (height / 100) ** 2


def get_pct(m=25, fm=25):
    return m / fm * 100

# get_pct = lambda m, fm: m / fm * 100

def get_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def print_status(bmi):
    if bmi < 18.5:
        print( "Underweight")
    elif bmi < 25:
        print( "Normal")
    elif bmi < 30:
        print( "Overweight")
    else:
        print( "Obese")
