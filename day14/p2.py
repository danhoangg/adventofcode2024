import re

with open('in', 'r') as f:
    lines = f.read().split('\n')


rows, cols = 103, 101
grid = [['.' for _ in range(cols)] for _ in range(rows)]

def line_exists(grid):
    for r in range(rows):
        for c in range(cols - 7):
            if ' ' not in grid[r][c:c+7]:
                return True
    return False

robots = []
regex = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
for l in lines:
    c, r, dc, dr = map(int, re.findall(regex, l)[0])
    robots.append([r, c, dr, dc])

for j in tqdm(range(10000)):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for i, (r, c, dr, dc) in enumerate(robots):
        robots[i][0] = (r + dr) % rows
        robots[i][1] = (c + dc) % cols

    for r, c, dr, dc in robots:
        if grid[r][c] == ' ':
            grid[r][c] = '1'
        else:
            grid[r][c] = str(int(grid[r][c]) + 1)

    if not line_exists(grid):
        continue
    tree = f'TREE {j + 1}\n'
    for r in range(rows):
        for c in range(cols):
            tree += grid[r][c]
        tree += '\n'

    with open('trees', 'a') as f:
        f.write(tree)

# I then look in the file and pray a tree's there
