def pfs(n):
    factors = []
    prime_factors = []
    for i in range(n):
        d = i+1
        if n % d == 0 and d not in factors:
            factors.append(d)

    for i in range(len(factors)):
        factors2 = []
        for k in range(factors[i]):
            d = k+1
            if factors[i] % d == 0:
                factors2.append(d)

                
        if len(factors2) == 2 and factors2[1] not in prime_factors:
            prime_factors.append(factors2[1])

    return prime_factors
        
answer = pfs(600851475143)
print(answer)
