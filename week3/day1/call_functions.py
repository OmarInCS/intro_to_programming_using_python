
from week3.day1.my_functions import get_bmi, get_status

# w, h = eval(input("Enter weight and height: "))
# bmi = get_bmi(w, h)
# status = get_status(w, h)
# print(f"BMI: {round(bmi, 2)}, Status: {status}")

print(get_status(65, 1.82))
print(get_status())
print(get_status(90))
print(get_status(height=1.8))