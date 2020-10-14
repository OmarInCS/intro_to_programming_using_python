
from week2.day4.my_functions import *

w, h = eval(input("Enter weight and height: "))

bmi = calc_bmi(w, h)
status = get_status(bmi)

print(status, bmi)
