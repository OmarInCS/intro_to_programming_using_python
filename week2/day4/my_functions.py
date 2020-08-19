
from termcolor import colored


def get_percentage(m=10, fm=50):
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


def print_grade(pct):
    print("PCT is:", pct, "grade:", end="\t")
    if pct > 85:
        print(colored("Excellent", "green"))
    elif pct > 75:
        print(colored("V. Good", "green"))
    elif pct > 65:
        print(colored("Good", "yellow"))
    elif pct >= 50:
        print(colored("Pass", "yellow"))
    else:
        print(colored("Fail", "red"))
