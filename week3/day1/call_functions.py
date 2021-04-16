
from week3.day1.my_functions import *

# w, h = eval(input("Enter weight and height: "))
#
# bmi = get_bmi(w, h)
# status = get_status(bmi)
#
# print(status, bmi)

fm = eval(input("Enter full mark: "))

print(get_percentage(23, 25))
print(get_percentage(23))
print(get_percentage(27, 30))
print(get_percentage())
print(get_percentage(full_mark=fm))
