with open('in', 'r') as f:
    lines = f.read().split('\n')

res = 0
for l in lines:
    a = list(map(int, l.split(' ')))

    m = 1 if a[0] < a[1] else -1
    for i in range(1, len(a)):
        if not (1 <= abs(a[i] - a[i - 1]) <= 3 and m * (a[i] - a[i - 1]) > 0):
            break
    else:
        res += 1

print(res)
