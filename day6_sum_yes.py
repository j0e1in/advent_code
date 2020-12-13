with open('input/day6.txt') as f:
    groups = f.read().strip().split('\n\n')

# Part 1
total = 0
for g in groups:
    anss = g.strip().split('\n')
    yess = set()
    for l in anss:
        yess |= set(list(l))
    total += len(yess)

print(total)

# Part 2
total = 0
for g in groups:
    anss = g.strip().split('\n')
    yess = set(anss[0])
    for l in anss[1:]:
        yess &= set(list(l))
    total += len(yess)

print(total)