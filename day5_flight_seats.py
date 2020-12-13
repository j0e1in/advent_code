with open('input/day5.txt') as f:
    tickets = f.read().strip().split('\n')

def get_row_num(ticket):
    row_range = [0, 127]
    for c in ticket:
        if c == 'F':
            row_range[1] = (row_range[0] + row_range[1]) // 2
        elif c == 'B':
            row_range[0] = (row_range[0] + row_range[1] + 1) // 2
    return row_range[0]


def get_col_num(ticket):
    col_range = [0, 7]
    for c in ticket:
        if c == 'L':
            col_range[1] = (col_range[0] + col_range[1]) // 2
        elif c == 'R':
            col_range[0] = (col_range[0] + col_range[1] + 1) // 2
    return col_range[0]

seats = []
for t in tickets:
    seats.append(get_row_num(t) * 8 + get_col_num(t))

# Part 1
print(max(seats))

# Part 2
seats.sort()
for i in range(0, len(seats)-1):
    if seats[i] != seats[i+1]-1:
        print(seats[i]+1)
