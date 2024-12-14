import re
from math import prod

with open('in', 'r') as f:
    lines = f.read().split('\n')

rows, cols = 103, 101
grid = [['.' for _ in range(cols)] for _ in range(rows)]
robots = []
regex = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
for l in lines:
    c, r, dc, dr = map(int, re.findall(regex, l)[0])
    robots.append([r, c, dr, dc])

for i, (r, c, dr, dc) in enumerate(robots):
    robots[i][0] = (r + dr * 100) % rows
    robots[i][1] = (c + dc * 100) % cols

for r, c, dr, dc in robots:
    if grid[r][c] == '.':
        grid[r][c] = '1'
    else:
        grid[r][c] = str(int(grid[r][c]) + 1)

res = [0, 0, 0, 0]
for r in range(rows):
    for c in range(cols):
        if r == rows // 2 or c == cols // 2:
            continue
        if grid[r][c] != '.':
            robots = int(grid[r][c])
            if r < rows / 2:
                if c < cols / 2:
                    res[0] += robots
                else:
                    res[1] += robots
            else:
                if c < cols / 2:
                    res[2] += robots
                else:
                    res[3] += robots

print(prod(res))
