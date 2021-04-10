
number = 2
print_count = 0

while print_count < 50:
    is_prime = True
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
        print_count += 1
    number += 1
