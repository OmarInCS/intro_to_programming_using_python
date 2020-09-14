
from random import randint

with open("words.txt") as file:
    words_list = file.readlines()

words_list = [w.strip() for w in words_list]
idx = randint(0, len(words_list))
correct_word = words_list[idx]
guess_word = correct_word[1:-1]
answer = input(f"Guess the word '_{guess_word}_': ")

if correct_word == answer:
    print("Correct")
else:
    print("Wrong, the word was:", correct_word)
