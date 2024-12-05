import collections

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
        if any(k in adj[a[j]] for k in a[:j]):
            return False
    return True

def topological_sort(a):
    f_adj = defaultdict(list)
    for u in a:
        if u in adj:
            f_adj[u] = [nei for nei in adj[u] if nei in a]

    degree = {u: 0 for u in a}
    for u in f_adj:
        for nei in f_adj[u]:
            degree[nei] += 1

    q = collections.deque([n for n in a if degree[n] == 0])
    sorted = []
    while q:
        u = q.popleft()
        sorted.append(u)
        for v in f_adj[u]:
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)

    return sorted

res = 0
while i < len(lines):
    a = list(map(int, lines[i].split(',')))

    if not ordered(a):
        res += topological_sort(a)[len(a) // 2]

    i += 1

print(res)
