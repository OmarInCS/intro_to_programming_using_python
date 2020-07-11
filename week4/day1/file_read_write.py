
# file = open("words.txt")
#
#
# file.close()

with open("words.txt") as file:
    # words = file.read()
    words = file.readlines()
    # word = file.readline()
    # word = file.readline()

lengths = [len(w.strip()) for w in words]
max_length = max(lengths)
min_length = min(lengths)

with open("words_stats.txt", "w") as file:
    file.write(f"Number of Words: {len(words)}\n")
    file.write(f"Max. word length: {max_length}\n")
    file.write(f"Min. word length: {min_length}\n")