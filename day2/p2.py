with open('in', 'r') as f:
    lines = f.read().split('\n')

def safe(a):
    m = 1 if a[0] < a[1] else -1
    for i in range(1, len(a)):
        if not (1 <= abs(a[i] - a[i - 1]) <= 3 and m * (a[i] - a[i - 1]) > 0):
            break
    else:
        return True

    return False

res = 0
for l in lines:
    a = list(map(int, l.split(' ')))

    for i in range(0, len(a) + 1):
        if safe(a[:i] + a[i+1:]):
            res += 1
            break

print(res)
