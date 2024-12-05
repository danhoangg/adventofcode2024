with open('in', 'r') as f:
    lines = f.read().split('\n')

adj = defaultdict(list)
i = 0
while lines[i] != '':
    a, b = map(int, lines[i].split('|'))
    adj[a].append(b)

    i += 1
i += 1

def ordered(a):
    for j in range(len(a) - 1, 0, -1):
        for k in range(j):
            if a[k] in adj[a[j]]:
                return False, j, k
    return True, -1, -1

res = 0
while i < len(lines):
    a = list(map(int, lines[i].split(',')))

    o, j, k = ordered(a)
    if o:
        i += 1
        continue

    while not o:
        t = a[j]
        a[j] = a[k]
        a[k] = t

        o, j, k = ordered(a)

    res += a[len(a) // 2]
    i += 1

print(res)
