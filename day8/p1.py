from itertools import combinations

with open('in', 'r') as f:
    grid = list(map(list, f.read().split('\n')))

a = defaultdict(list)
rows, cols = len(grid), len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '.':
            a[grid[r][c]].append((r, c))

res = set()
for freq, coords in a.items():
    for c1, c2 in combinations(coords, 2):
        dr, dc = c1[0] - c2[0], c1[1] - c2[1]

        nr, nc = c1[0] + dr, c1[1] + dc
        if nr in range(rows) and nc in range(cols):
            res.add((nr, nc))

        nr, nc = c2[0] - dr, c2[1] - dc
        if nr in range(rows) and nc in range(cols):
            res.add((nr, nc))

print(len(res))
