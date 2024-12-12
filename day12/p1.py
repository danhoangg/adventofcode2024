import collections

with open('in', 'r') as f:
    grid = list(map(list, f.read().split('\n')))

rows, cols = len(grid), len(grid[0])
visited = set()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(r, c):
    q = collections.deque()

    visited.add((r, c))
    q.append((r, c))
    t = grid[r][c]

    area, perimeter = 0, 0
    while q:
        r, c = q.popleft()
        area += 1
        nei = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(rows) and nc in range(cols) and grid[nr][nc] == t:
                nei += 1
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

        perimeter += 4 - nei

    return area, perimeter

res = 0
for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            area, perimeter = bfs(r, c)
            res += area * perimeter

print(res)
