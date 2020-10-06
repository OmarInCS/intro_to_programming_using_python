
weight = eval(input("Enter your weight: "))
height = eval(input("Enter your height: "))

bmi = weight / height ** 2

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
