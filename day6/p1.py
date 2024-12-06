with open('in', 'r') as f:
    grid = list(map(list, f.read().split('\n')))

rows, cols = len(grid), len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '^':
            start = (r, c)
            break
    else:
        continue
    break

dr, dc = -1, 0
r, c = start
visited = set()
while r in range(rows) and c in range(cols):
    visited.add((r, c))
    nr, nc = r + dr, c + dc
    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '#':
        dr, dc = dc, -dr

    r += dr
    c += dc

print(len(visited))
