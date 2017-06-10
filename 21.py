def find_divisors(n):
    divisors = []
   
    for d in range(1, int(n**0.5+1)):
        if n % d == 0 and n!= d and d not in divisors:
            divisors.append(d)
            divisors.append(int(n/d))

    divisors.remove(n) #n is a divisor, but only divisors < n are wanted
    return divisors


def d(n):
    return sum(find_divisors(n))

amicables = []

for a in range(2, 10000):
    for b in range(2, 10000):

        if d(a) == b and d(b) == a and a != b:
            #isAmicable = True
            if d(a) not in amicables:
                amicables.append(a)
            if d(b) not in amicables:
                amicables.append(a)
#print(amicables)

answer = sum(amicables)
print(answer)
