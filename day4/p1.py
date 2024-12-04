with open('in', 'r') as f:
    grid = [list(i) for i in f.read().split('\n')]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]

t = 'XMAS'

rows, cols = len(grid), len(grid[0])

def dfs(r, c, dr, dc, i):
    if r not in range(rows) or c not in range(cols):
        return False
    if grid[r][c] != t[i]:
        return False
    if i == 3:
        return True

    return dfs(r + dr, c + dc, dr, dc, i + 1)

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'X':
            for dr, dc in directions:
                if dfs(r, c, dr, dc, 0):
                    res += 1

print(res)
