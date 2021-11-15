
salaries = [5000, 13000, 7000, 15000]
salaries_count = {"high": 0, "normal": 0, "low": 0}

for sal in salaries:
    if sal >= 12000:
        salaries_count["high"] += 1
    elif sal >= 6000:
        salaries_count["normal"] += 1
    else:
        salaries_count["low"] += 1

for level, count in salaries_count.items():
    print(level, "=>", count)
