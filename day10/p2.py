with open('in', 'r') as f:
    grid = [list(map(int, line.strip())) for line in f]

rows, cols = len(grid), len(grid[0])
start = []
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            start.append((r, c))

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
res = [0]
def dfs(r, c):
    if grid[r][c] == 9:
        res[0] += 1
        return

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr in range(rows) and nc in range(cols) and (nr, nc) and grid[nr][nc] == grid[r][c] + 1:
            dfs(nr, nc)

for r, c in start:
    dfs(r, c)

print(res[0])
