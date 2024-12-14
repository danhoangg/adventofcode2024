import re

with open('in', 'r') as f:
    machines = f.read().split('\n\n')

res = 0
for m in machines:
    lines = m.split('\n')
    a = list(map(int, list(*re.findall(r'\+(\d+).*\+(\d+)$', lines[0]))))
    b = list(map(int, list(*re.findall(r'\+(\d+).*\+(\d+)$', lines[1]))))
    target = list(map(int, list(*re.findall(r'=(\d+).*=(\d+)$', lines[2]))))

    D = (b[0] * a[1] - a[0] * b[1])
    if (b[1] * target[0] - target[1] * b[0]) / D == (b[1] * target[0] - target[1] * b[0]) // D and (a[0] * target[1] - a[1] * target[0]) / D == (a[0] * target[1] - a[1] * target[0]) // D:
        res += (a[0] * target[1] - a[1] * target[0]) // D
        res += 3 * ((b[1] * target[0] - target[1] * b[0]) // D)

print(-res)
