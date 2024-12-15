import collections

with open('in', 'r') as f:
    maze, instructions = f.read().split('\n\n')

grid = []
for i, line in enumerate(maze.split('\n')):
    t = []
    for j, c in enumerate(line):
        if c == '#':
            t += ['#', '#']
        elif c == 'O':
            t += ['[', ']']
        elif c == '.':
            t += ['.', '.']
        else:
            t += ['.', '.']
            start = (i, j * 2)
    grid.append(t)

rows, cols = len(grid), len(grid[0])

instructions = ''.join(instructions.split('\n'))
directions = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

def move_boxes(r, c, dr, dc):
    s = []
    q = collections.deque()
    visited = set()

    q.append((r, c))
    visited.add((r, c))
    if grid[r][c] == '[':
        q.append((r, c + 1))
        visited.add((r, c + 1))
    else:
        q.append((r, c - 1))
        visited.add((r, c - 1))

    while q:
        r, c = q.popleft()
        s.append((r, c))
        nr, nc = r + dr, c + dc

        if grid[nr][nc] == '#':
            return False

        if grid[nr][nc] == '[' and (nr, nc) not in visited:
            q.append((nr, nc))
            q.append((nr, nc + 1))
            visited.add((nr, nc))
            visited.add((nr, nc + 1))
        elif grid[nr][nc] == ']' and (nr, nc) not in visited:
            q.append((nr, nc))
            q.append((nr, nc - 1))
            visited.add((nr, nc))
            visited.add((nr, nc - 1))

    while s:
        r, c = s.pop()
        grid[r + dr][c + dc] = grid[r][c]
        grid[r][c] = '.'

    return True

r, c = start
for i in instructions:
    dr, dc = directions[i]
    nr, nc = r + dr, c + dc

    if grid[nr][nc] == '.':
        r, c = nr, nc
    elif grid[nr][nc] in '[]':
        if move_boxes(nr, nc, dr, dc):
            r, c = nr, nc

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '[':
            res += r * 100 + c
print(res)
