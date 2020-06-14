
from week2.day4.my_functions import *


# w, h = eval(input("Enter weight and height: "))
# bmi = get_bmi(w, h)
# print("BMI:", bmi)
# print("Status:", get_status(bmi))

# pct = get_pct(20, 25)
# print("PCT:", pct)
# grade = get_grade(pct)
# print("Grade:", grade)

print(get_pct())
print(get_pct(23, 25))
print(get_pct(23))
print(get_pct(final_mark=25))

print(get_bmi(65, 1.82))