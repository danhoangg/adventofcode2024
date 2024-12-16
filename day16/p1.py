import heapq

with open('in', 'r') as f:
    lines = f.read().split('\n')

grid = list(map(list, lines))
rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            grid[r][c] = '.'
            start = (r, c)
        if grid[r][c] == "E":
            grid[r][c] = '.'
            target = (r, c)

pq = []
visited = set()
heapq.heappush(pq, (0, *start, 0, 1))
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
while pq:
    w, r, c, fr, fc = heapq.heappop(pq)
    visited.add((r, c, fr, fc))
    if (r, c) == target:
        print(w)
        break
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr in range(rows) and nc in range(cols) and (nr, nc, dr, dc) not in visited and grid[nr][nc] == '.':
            if (dr, dc) == (fr, fc):
                heapq.heappush(pq, (w + 1, nr, nc, dr, dc))
            else:
                heapq.heappush(pq, (w + 1001, nr, nc, dr, dc))
              
