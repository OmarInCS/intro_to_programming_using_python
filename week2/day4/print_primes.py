
def is_prime(number):

    if number <= 1:
        return False

    for div in range(2, number):
        if number % div == 0:
            return False

    return True


number = 2
print_count = 0

while print_count < 50:
    if is_prime(number):
        print(number, end="\t")
        print_count += 1
        if print_count % 10 == 0:
            print()
    number += 1
