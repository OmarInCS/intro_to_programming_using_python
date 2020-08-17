
n = eval(input("Enter number of patients: "))
obese_count = 0

for i in range(n):
    w, h = eval(input("Enter ur weight and height: "))
    bmi = w / h ** 2
    print("BMI:", bmi)

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")
        obese_count += 1

    print("-" * 30)

print("#Obese:", obese_count)