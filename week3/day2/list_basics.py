
scores = [23, 15, 20, 24]

print(scores)
print(len(scores))
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
print(scores[0])
print(scores[3])
print(scores[-1])

scores.append(10)
print(scores)
scores.insert(0, 17)
print(scores)
scores.sort(reverse=True)
print(scores)

print(scores[:3])
print(scores[-3:])

scores.remove(10)
print(scores)
scores.pop(-1)
print(scores)

print(23 in scores)

for i in range(len(scores)):
    scores[i] += 1

print(scores)

# for i in range(len(scores)):
#     print(scores[i])

for v in scores:
    print(v)