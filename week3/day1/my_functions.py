
# def get_percentage(mark=20, full_mark=20):
#     return mark / full_mark * 100

get_percentage = lambda m=20, fm=20: m / fm * 100

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

def print_status(bmi):
    if bmi < 18.5:
        print( "Underweight")
    elif bmi < 25:
        print ("Normal")
    elif bmi < 30:
        print ("Overweight")
    else:
        print ("Obese")
