fractional = ""
for n in range(1, 1000001):
    fractional = fractional+str(n)

answer = 1
for p in range(7):
    answer *= int(fractional[(10**p)-1])

print(answer)
