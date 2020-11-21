
def get_percentage(mark=100, final_mark=100):
    return mark / final_mark * 100


def get_grade(pct):
    if pct >= 85:
        return "Excellent"
    elif pct >= 75:
        return "V. Good"
    elif pct >= 65:
        return "Good"
    elif pct >= 50:
        return "Pass"
    else:
        return "Fail"


