r = 1000000

def rotate(n):
    n_list = [int(x) for x in str(n)]
    rotations = []
    for digit in range(len(str(n))):
        rotations.append(int(''.join(map(str,n_list))))
        n_list.append(n_list.pop(0))
        
    return rotations


def gen_primes(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

print("Generating primes below {}...".format(r))
primes = gen_primes(r)
print("Primes generated...")
circular_primes = []

print()
print("Calculating circular primes below {}...".format(r))
for prime in primes:
    rotations = rotate(prime)
    primes_in_rotations = 0
    for i in rotations:
        if i not in primes:
            break
        else:
            primes_in_rotations += 1

        if primes_in_rotations == len(rotations) and prime not in circular_primes:
            circular_primes.append(prime)
            print("{} added!".format(str(prime)))

answer = len(circular_primes)
print("Complete! There are {} circular primes below {}".format(str(answer), str(r)))
