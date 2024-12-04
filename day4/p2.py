with open('in', 'r') as f:
    grid = [list(i) for i in f.read().split('\n')]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
rows, cols = len(grid), len(grid[0])
t = ['MSAMS', 'SSAMM', 'SMASM', 'MMASS']

res = 0
for r in range(rows - 2):
    for c in range(cols - 2):
        cur = ''.join([grid[r][c], grid[r][c + 2], grid[r + 1][c + 1], grid[r + 2][c], grid[r + 2][c + 2]])
        if cur in t:
            res += 1

print(res)
