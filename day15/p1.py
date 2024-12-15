with open('in', 'r') as f:
    maze, instructions = f.read().split('\n\n')

grid = []
for i, line in enumerate(maze.split('\n')):
    t = []
    for j, c in enumerate(line):
        if c == '#':
            t.append(1)
        elif c == 'O':
            t.append(2)
        elif c == '.':
            t.append(0)
        else:
            t.append(0)
            start = (i, j)
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
    boxes = []
    while grid[r][c] == 2:
        boxes.append((r, c))
        r += dr
        c += dc

    if grid[r][c] == 1:
        return False

    for br, bc in reversed(boxes):
        grid[br + dr][bc + dc] = 2
        grid[br][bc] = 0

    return True

r, c = start
for i in instructions:
    dr, dc = directions[i]
    nr, nc = r + dr, c + dc

    if grid[nr][nc] == 0:
        r, c = nr, nc
    elif grid[nr][nc] == 2:
        if move_boxes(nr, nc, dr, dc):
            r, c = nr, nc

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 2:
            res += 100 * r + c
          
print(res)
