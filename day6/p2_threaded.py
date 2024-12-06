from pqdm.processes import pqdm

with open('in', 'r') as f:
    grid = list(map(list, f.read().split('\n')))

rows, cols = len(grid), len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '^':
            start = (r, c)
            grid[r][c] = '.'
            break
    else:
        continue
    break

def loop(grid):
    r, c = start
    dr, dc = -1, 0

    visited = set()
    while r in range(rows) and c in range(cols):
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        nr, nc = r + dr, c + dc
        if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '#':
            dr, dc = dc, -dr
        else:
            r += dr
            c += dc

    return False

def change_grid(replace):
    cr, cc = replace
    modified_grid = [i.copy() for i in grid]
    modified_grid[cr][cc] = '#'
    return loop(modified_grid)

if __name__ == '__main__':
    spaces = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '.']
    res = pqdm(spaces, change_grid, n_jobs=20)
    print(res.count(True))
