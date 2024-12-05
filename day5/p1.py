with open('in', 'r') as f:
    lines = f.read().split('\n')

adj = defaultdict(list)
i = 0
while lines[i] != '':
    a, b = map(int, lines[i].split('|'))
    adj[a].append(b)

    i += 1
i += 1

res = 0
while i < len(lines):
    a = list(map(int, lines[i].split(',')))

    for j in range(len(a) - 1, 0, -1):
        if any(i in adj[a[j]] for i in a[:j]):
            break
    else:
        res += a[len(a) // 2]
    i += 1

print(res)
