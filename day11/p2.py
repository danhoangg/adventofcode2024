from collections import Counter

with open('in', 'r') as f:
    a = list(f.read().split(' '))

d = Counter(a)

dp = {}
def blink(n):
    if n in dp:
        return dp[n]

    if n == '0':
        res = ['1']
    elif len(n) % 2 == 0:
        res =  [str(int(n[len(n) // 2:])), str(int(n[:len(n) // 2]))]
    else:
        res = [str(int(n) * 2024)]

    dp[n] = res
    return res

for i in range(75):
    t = defaultdict(int)
    for n, c in d.items():
        for j in blink(n):
            t[j] += c
    d = t

res = 0
for n in d:
    res += d[n]

print(res)
