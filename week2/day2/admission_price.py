
nb_of_people = eval(input("Enter the #people: "))

price = 0

for i in range(nb_of_people):
    age = eval(input("Enter the age: "))
    if age < 2:
        price += 0
    elif age >= 3 and age <= 12:
        price += 14
    elif age >= 65:
        price += 18
    else:
        price += 23

print("Total Price:", price)