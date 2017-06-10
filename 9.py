a, b, c = 0, 0, 0

for a in range(333):                #For speed, set range to (198,202)
    for b in range(1000):
        for c in range(1000):
            if (a < b) and (b < c) and (a**2 + b**2 == c**2) and a+b+c == 1000:
                answer = a*b*c
                
print(answer)
