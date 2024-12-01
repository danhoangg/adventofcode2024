with open('in', 'r') as f:
    lines = f.read().split('\n')

a, b = {}, {}
for l in lines:
    n, m = map(int, l.split('   '))

    if n not in a:
        a[n] = 0
    if m not in b:
        b[m] = 0
    a[n] += 1
    b[m] += 1

res = 0
for n, c in a.items():
    if n in b:
        res += n * c * b[n]

print(res)
