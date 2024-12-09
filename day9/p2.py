with open('in', 'r') as f:
    inp = f.read()

file, id = True, 0
d, sizes, spaces = [], {}, {}
for n in inp:
    if file:
        sizes[id] = (int(n), len(d))
        d += [id] * int(n)
        id += 1
    elif int(n) != 0:
        spaces[len(d)] = int(n)
        d += [-1] * int(n)

    file = not file

sizes = sorted(sizes.items(), reverse=True)
for id, (size, ix) in sizes:
    s = sorted(spaces.items())
    for i, space in s:
        if space >= size:
            break
    else:
        continue
    if i >= ix:
        continue

    d[i:i+size], d[ix:ix+size] = d[ix:ix+size], d[i:i+size]
    del spaces[i]
    space -= size
    i += size
    if space != 0:
        spaces[i] = space

res = 0
for i in range(len(d)):
    if d[i] != -1:
        res += i * d[i]

print(res)
