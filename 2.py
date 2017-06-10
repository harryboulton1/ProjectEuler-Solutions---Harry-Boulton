final_terms = []

a = 1
b = 2

for i in range(100):
    i=i
    if a < 4000000 and a % 2 == 0:
            final_terms.append(a)
    if b < 4000000 and b % 2 == 0:
            final_terms.append(b)
    a = a + b
    b = a + b

answer = sum(final_terms)

print(answer)
