
salaries = [13000, 5000, 7000, 15000]
level_counts = {
    "High": 0,
    "Normal": 0,
    "Low": 0
}

for s in salaries:
    if s >= 12000:
        level_counts["High"] += 1
    elif s >= 6000:
        level_counts["Normal"] += 1
    else:
        level_counts["Low"] += 1

with open("salaries_report.txt", "w") as file:
    for level, count in level_counts.items():
        file.write(f"{level} => {count}\n")
