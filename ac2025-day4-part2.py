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

def clear_removed(to_be_removed):
    for line in to_be_removed:
        temp = grid[line[0]]
        temp = temp[:line[1]] + '.' + temp[line[1]+1:]
        grid[line[0]] = temp

available = 0
removed = 0
with open("data-2025-day4.txt", "r") as f:
    available = 0
    grid = [line.rstrip() for line in f]
    while True:
        to_remove = []
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '@':
                    if count_neighbors(row, col) < 4:
                        available += 1
                        to_remove.append([row, col])
        clear_removed(to_remove)
        removed += len(to_remove)
        if not to_remove:
            break
print(removed)
