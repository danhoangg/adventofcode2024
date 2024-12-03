import re

with open('in', 'r') as f:
    inp = f.read()

regex = r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)"
m = re.findall(regex, inp)

mul = lambda x, y: x * y
res = 0
execute = True
for f in m:
    if f == "don't()":
        execute = False
    elif f == "do()":
        execute = True
    else:
        res += eval(f) if execute else 0

print(res)
