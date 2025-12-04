def count_neighbors(row, col):
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    count = 0
    for dir_r, dir_c in directions:
        neigh_row, neigh_col = row + dir_r, col + dir_c
        if 0 <= neigh_row < rows and 0 <= neigh_col < cols:
            if grid[neigh_row][neigh_col] == '@':
                count += 1
    return count

available = 0
with open("data-2025-day4.txt", "r") as f:
    available = 0
    grid = [line.rstrip() for line in f]
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                if count_neighbors(row, col) < 4:
                    available += 1
print(available)