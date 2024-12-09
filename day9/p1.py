with open('in', 'r') as f:
    inp = f.read()

file, id = True, 0
d = []
for n in inp:
    if file:
        d += [id] * int(n)
        id += 1
    else:
        d += [-1] * int(n)

    file = not file

l, r = 0, len(d) - 1
while d[l] != -1:
    l += 1

while l < r:
    d[l], d[r] = d[r], d[l]
    r -= 1

    while d[l] != -1:
        l += 1

res, i = 0, 0
while d[i] != -1:
    res += d[i] * i
    i += 1

print(res)
