with open("data-2025-day6.txt", "r", encoding="utf-8") as f:
    grid = [line.rstrip("\n") for line in f.readlines()]

total = 0
rows = len(grid)
cols = len(grid[0])

separator_cols = [
    c for c in range(cols)
    if all(grid[r][c] == ' ' for r in range(rows))
]

segments = []
prev = -1
for s in separator_cols + [cols]:
    if s - prev > 1:
        segments.append((prev + 1, s - 1))
    prev = s
segments = segments[::-1]

last_row = grid[-1]
results = []

for start, end in segments:
    ops_here = [last_row[c] for c in range(start, end + 1) if last_row[c] != ' ']
    if not ops_here:
        continue
    op_char = ops_here[0]
    numbers = []
    for c in range(end, start - 1, -1):
        digits = ''.join(
            grid[r][c] for r in range(rows - 1)
            if grid[r][c] != ' '
        )
        if digits:
            numbers.append(int(digits))

    if op_char == "+":
        value = sum(numbers)
    else:
        value = 1
        for i in numbers:
            value *= i
    total += value

print(total)