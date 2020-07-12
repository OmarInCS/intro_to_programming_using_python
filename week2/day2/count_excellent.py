
final_mark = eval(input("What's exam final mark? "))
count = eval(input("How many student? "))
excellent = 0

for i in range(count):
    mark = eval(input(f"Enter mark of student {i+1}: "))
    pct = mark / final_mark * 100
    if pct > 85:
        excellent += 1

print("Number of excellents:", excellent)