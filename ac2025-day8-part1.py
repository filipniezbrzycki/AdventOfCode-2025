
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True

    def componentSizes(self):
        rootToSize = defaultdict(int)
        for i in range(len(self.parent)):
            r = self.find(i)
            rootToSize[r] += 1
        return list(rootToSize.values())

coords = []
with open("data-2025-day8.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        x, y, z = map(int, parts)
        coords.append((x, y, z))
nrOfPoints = len(coords)
uf = UnionFind(nrOfPoints)
edges = []
for i in range(nrOfPoints):
    x1, y1, z1 = coords[i]
    for j in range(i + 1, nrOfPoints):
        x2, y2, z2 = coords[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        d2 = dx * dx + dy * dy + dz * dz
        edges.append((d2, i, j))
edges.sort(key=lambda e: e[0])
limit = 1000
for k in range(limit):
    _, i, j = edges[k]
    uf.union(i, j)
sizes = sorted(uf.componentSizes(), reverse=True)
production = sizes[0] * sizes[1] * sizes[2]
print(sizes[0] * sizes[1] * sizes[2])