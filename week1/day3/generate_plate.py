#05 99 888 921
from random import randint

plate = chr(randint(65, 90))
plate += chr(randint(65, 90))
plate += chr(randint(65, 90))
plate += str(randint(1, 9999))

print(plate)
