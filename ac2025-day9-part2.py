def point_on_segment(px, py, x1, y1, x2, y2):
    if (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1) != 0:
        return False
    return (min(x1, x2) <= px <= max(x1, x2) and
            min(y1, y2) <= py <= max(y1, y2))

def point_in_polygon(px, py, polygon):
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if point_on_segment(px, py, x1, y1, x2, y2):
            return True
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            x_intersect = (x2 - x1) * (py - y1) / (y2 - y1) + x1
            if px < x_intersect:
                inside = not inside
    return inside

def rectangle_fully_inside_polygon(x1, y1, x2, y2, polygon):
    if x1 == x2 or y1 == y2:
        return False
    min_x, max_x = sorted((x1, x2))
    min_y, max_y = sorted((y1, y2))
    cx = (min_x + max_x) / 2.0
    cy = (min_y + max_y) / 2.0
    if not point_in_polygon(cx, cy, polygon):
        return False
    n = len(polygon)
    for i in range(n):
        ax, ay = polygon[i]
        bx, by = polygon[(i + 1) % n]
        if ax == bx:
            x0 = ax
            if min_x < x0 < max_x:
                lowy, highy = sorted((ay, by))
                if highy > min_y and lowy < max_y:
                    return False
        else:
            y0 = ay
            if min_y < y0 < max_y:
                lowx, highx = sorted((ax, bx))
                if highx > min_x and lowx < max_x:
                    return False
    return True

points = []
with open("data-2025-day9.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        points.append((int(parts[0]), int(parts[1])))
max_area = 0
for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        if not rectangle_fully_inside_polygon(x1, y1, x2, y2, points):
            continue
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area > max_area:
            max_area = area
print(max_area)
