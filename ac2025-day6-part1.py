total = 0
with open("data-2025-day6.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

rows = [line.split() for line in lines]

operations = rows[-1]
data = rows[:-1]

for index, operation in enumerate(operations):
    numbers = [int(row[index]) for row in data]
    if operation == '+':
        column_result = sum(numbers)
    else:
        column_result = 1
        for n in numbers:
            column_result *= n
    total += column_result
print(total)

