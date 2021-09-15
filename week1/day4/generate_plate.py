
from random import randint

# plate = randint(65, 90)
# print(plate)
plate = chr(randint(65, 90))
plate += chr(randint(65, 90))
plate += chr(randint(65, 90))
plate += str(randint(1, 9999))
print(plate)