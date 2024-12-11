with open('in', 'r') as f:
    a = list(map(int, f.read().split(' ')))

def blink(a):
    t = []
    for i in range(len(a)):
        if a[i] == 0:
            t.append(1)
            continue
        l = len(str(a[i]))
        if l % 2 == 0:
            t += [int(str(a[i])[:l // 2]), int(str(a[i])[l // 2:])]
        else:
            t.append(a[i] * 2024)
    return t

for i in range(25):
    a = blink(a)

print(len(a))
