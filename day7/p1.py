with open('in', 'r') as f:
    lines = f.read().split('\n')

def dfs(cur, curlist, t):
    if not curlist:
        if cur == t:
            return True
        else:
            return False

    return dfs(cur * curlist[0], curlist[1:], t) or dfs(cur + curlist[0], curlist[1:], t)

res = 0
for l in lines:
    t = int(l.split(':')[0])
    a = list(map(int, l.split(' ')[1:]))

    if dfs(0, a, t):
        res += t

print(res)
