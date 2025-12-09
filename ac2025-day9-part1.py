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
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area > max_area:
            max_area = area

print(max_area)
