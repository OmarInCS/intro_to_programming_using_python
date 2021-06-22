
weight = eval(input("Enter your weight: "))
height = eval(input("Enter your height: "))

bmi = weight / (height / 100) ** 2
print("BMI:", bmi)
