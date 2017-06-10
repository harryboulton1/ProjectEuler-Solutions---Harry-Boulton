import itertools
permutations = [list(i) for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9])]

primes = [2,3,5,7,11,13,17]
def concat(digits, i):
    return int(str(digits[i+1])+str(digits[i+2])+str(digits[i+3]))

solutions = []
for n in permutations:
    digits = {}
    for digit in n:
        digits[digit+1] = n[digit]


    count = 0
    for i in range(1,8):
        #print(i+1, i+2, i+3)
        #print(primes[i-1])
        triplet = concat(digits,i)
        if triplet % primes[i-1] == 0:
            count += 1
        #if int("".join(digits[i+1],digits[i+2],digits[i+3])) % primes[i-1] == 0:
        #    count += 1
            #print(count)

    if count == 7:
        solution = int(''.join(str(i) for i in n))
        solutions.append(solution)

answer = sum(solutions)
print(answer)
