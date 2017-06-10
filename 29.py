LB = 2
UB = 100

terms = []
for base in range (LB, UB+1):
    for power in range(LB, UB+1):
        x = base**power
        if x not in terms:
            terms.append(x)

answer = len(terms)
print(answer)
