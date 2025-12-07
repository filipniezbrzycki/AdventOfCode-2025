with open("data-2025-day7.txt", "r") as f:
    tachyonManifold = [line.rstrip() for line in f.readlines()]
height = len(tachyonManifold)
width = len(tachyonManifold[0])
start_col = tachyonManifold[0].index("S")
distinctPaths = [[0] * width for _ in range(height + 1)]
for c in range(width):
    distinctPaths[height][c] = 1
for r in range(height-1, 0, -1):
    row = tachyonManifold[r]
    for c in range(width):
        cell = row[c]
        if cell == '.':
            distinctPaths[r][c] = distinctPaths[r + 1][c]
        else:
            total = 0
            if c - 1 >= 0:
                total += distinctPaths[r + 1][c - 1]
            if c + 1 < width:
                total += distinctPaths[r + 1][c + 1]
            distinctPaths[r][c] = total
print(distinctPaths[1][start_col])