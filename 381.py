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

def fct(n):
    x = 1
    for i in range(1,n+1):
        x*=i
    return x

def S(p):
    a = 0
    for k in range(1,6):
        a += fct(p-k)
    return a%p

def removePrimes(primes, lower):   
    while primes[0] < lower:
        primes.pop(0)

    return primes

def rangedPrimes(lower, upper):
    primes = gen_primes(upper)                  
    primes = removePrimes(primes, lower)
    return primes

def sumSp(lower, upper):
    primes = rangedPrimes(lower, upper) #primes:     lower <= p < upper

    sumSp = 0
    for p in primes:
        sumSp += S(p)
    return sumSp
