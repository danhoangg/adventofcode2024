import re

with open('in', 'r') as f:
    inp = f.read()

regex = r'mul\([0-9]+,[0-9]+\)'
m = re.findall(regex, inp)

mul = lambda x, y: x * y
res = sum(map(eval, m))

print(res)
