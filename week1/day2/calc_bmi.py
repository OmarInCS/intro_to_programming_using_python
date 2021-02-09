
weight, height = eval(input("Enter weight and height: "))

bmi = weight / height ** 2

print("BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")