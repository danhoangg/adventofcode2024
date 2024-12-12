import collections

with open('in', 'r') as f:
    grid = list(map(list, f.read().split('\n')))

rows, cols = len(grid), len(grid[0])
visited = set()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def count_sides(squares):
    edges = set()
    for r, c in squares:
        for dr, dc in directions:
            if (r + dr, c + dc) not in squares:
                edges.add(((r + dr, c + dc), (r, c)))

    res = len(edges)
    completed = set()
    for (r, c), (dr, dc) in edges:
        if c == dc:
            if ((r, c + 1), (dr, dc + 1)) in edges and ((r, c + 1), (dr, dc + 1)) not in completed:
                res -= 1
            if ((r, c - 1), (dr, dc - 1)) in edges and ((r, c - 1), (dr, dc - 1)) not in completed:
                res -= 1
        elif r == dr:
            if ((r + 1, c), (dr + 1, dc)) in edges and ((r + 1, c), (dr + 1, dc)) not in completed:
                res -= 1
            if ((r - 1, c), (dr - 1, dc)) in edges and ((r - 1, c), (dr - 1, dc)) not in completed:
                res -= 1
        completed.add(((r, c), (dr, dc)))
    return res

def bfs(r, c):
    q = collections.deque()

    visited.add((r, c))
    q.append((r, c))
    t = grid[r][c]
    squares = set()

    area = 0
    while q:
        r, c = q.popleft()
        squares.add((r, c))
        area += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == t:
                visited.add((nr, nc))
                q.append((nr, nc))

    return area, count_sides(squares)

res = 0
for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            area, perimeter = bfs(r, c)
            res += area * perimeter

print(res)
