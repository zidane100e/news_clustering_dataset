import random

f1_s = '1b.txt'
f2_s = '1c.txt'

lines = []
with open(f1_s) as f1:
    for line in f1:
        if line.strip() == '':
            continue
        lines.append(line)

random.shuffle(lines)
with open(f2_s, 'w') as f2:
    for line in lines[:130]:
        f2.write(line)
        