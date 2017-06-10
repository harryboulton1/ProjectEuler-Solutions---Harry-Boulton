def generate_spiral(size):
    grid = [([0 for columns in range(size)]) for rows in range(size)]       
    return grid

def next_shift(shift):
    if shift > 0:
        shift = -1*(shift+1)
    elif shift < 0:
        shift = -1*(shift-1)
    return shift

size = 5
spiral = generate_spiral(size)

c = int(size/2 + 1)
start = spiral[c][c]
