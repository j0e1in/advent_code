import math

with open("input/day3.txt") as f:
    grid = [[c for c in l] for l in f.read().split("\n") if l]

for i in range(len(grid)):
    assert len(grid[0]) == len(grid[i]), f"{i}: {len(grid[0])} != {len(grid[i])}"

print(f"Board size: {len(grid)} x {len(grid[0])}")

def count_trees(inp, steps):
    x, y = 0, 0
    count = 0
    while y < len(inp)-1:
        x = (x + steps[0]) % len(inp[0])
        y += steps[1]
        if inp[y][x] == '#':
            count += 1
    return count

print(count_trees(grid, (3, 1))) # part 1
print(math.prod([count_trees(grid, steps) for steps in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))