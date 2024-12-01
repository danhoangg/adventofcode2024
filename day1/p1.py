with open('in', 'r') as f:
    lines = f.read().split('\n')

a, b = [], []
for l in lines:
    n, m = map(int, l.split('   '))

    a.append(n)
    b.append(m)

a.sort()
b.sort()

res = 0
for i in range(len(a)):
    res += abs(a[i] - b[i])

print(res)
