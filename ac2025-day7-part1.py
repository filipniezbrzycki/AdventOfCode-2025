splits = 0
with open("data-2025-day7.txt", "r") as f:
    tachyonManifold = [line.rstrip() for line in f.readlines()]
height = len(tachyonManifold)
width = len(tachyonManifold[0])
startCol = tachyonManifold[0].index("S")
beams = [False] * width
beams[startCol] = True
for r in range(1, height):
    new_beams = [False] * width
    for c in range(width):
        if not beams[c]:
            continue
        cell = tachyonManifold[r][c]
        if cell == '.':
            new_beams[c] = True
        elif cell == '^':
            splits += 1
            if c - 1 >= 0:
                new_beams[c - 1] = True
            if c + 1 < width:
                new_beams[c + 1] = True
    beams = new_beams
print(splits)