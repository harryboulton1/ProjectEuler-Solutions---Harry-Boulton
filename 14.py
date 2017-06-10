def evaluate_length(n):

    count = 1
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3*n + 1)

        count += 1
    return count

lengths = {}
for n in range(1,1000000):
    lengths[n] = (evaluate_length(n))

lengths_sorted = sorted(lengths.values())
longest = lengths_sorted[-1]

for x in lengths.keys():
    if lengths[x] == longest:
        answer = x

print(answer)
