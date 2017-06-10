import math
    
count = 2
primes = []

while count < 2000000:
    isprime = True
    
    for x in range(2, int(count**0.5 + 1)):
        if count % x == 0: 
            isprime = False
            break
    
    if isprime:
        primes.append(count)
    else:
        pass
    
    count += 1

answer = sum(primes)

print(answer)
