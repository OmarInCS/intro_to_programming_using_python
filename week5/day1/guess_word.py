
from random import choice, randint

with open("words.txt") as file:
    words = file.readlines()

words = [w.strip() for w in words]
selected_word = list(choice(words))
correct_word = selected_word.copy()
idx = randint(0, len(selected_word) - 1)
selected_word[idx] = "?"
# print(correct_word)
answer = input(f"Guess the word {''.join(selected_word)}: ")

with open("scores.csv", "a") as file:
    file.write(''.join(correct_word) + ",")
    if answer == ''.join(correct_word):
        print("Correct")
        file.write("Correct\n")
    else:
        print("Wrong")
        file.write("Wrong\n")