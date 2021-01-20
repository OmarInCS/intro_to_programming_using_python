
def get_pct(mark=40, final_mark=40):
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


def get_number(char):
    if char in "abc":
        print(2, end="")
    elif char in "def":
        print(3, end="")
    elif char in "ghi":
        print(4, end="")
    elif char in "jkl":
        print(5, end="")
    elif char in "mno":
        print(6, end="")
    elif char in "pqrs":
        print(7, end="")
    elif char in "tuv":
        print(8, end="")
    elif char in "wxyz":
        print(9, end="")
    else:
        print(char, end="")