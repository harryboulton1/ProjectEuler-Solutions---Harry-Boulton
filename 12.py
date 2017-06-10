n, t= 0,0

factors = []
while len(factors) < 500:
    n += 1
    t += n

    factors = []
    for divisor in range(1, int((t**0.5)+1)):
        if t % divisor == 0 and divisor not in factors:
            factors.append(divisor)
            factors.append(int(t/divisor))

print(t)
