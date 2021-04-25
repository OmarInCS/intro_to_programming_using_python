
from day6.my_functions import *

weight, height = eval(input("Enter weight and height: "))
bmi = get_bmi(weight, height)
status = get_status(bmi)

print(status, bmi)
