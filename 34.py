r = 100000

def factorial(n):
    x = 1
    for i in range(n):
        x *= i+1
    return x
        
values = []
for n in range(r):
    digits = [int(x) for x in str(n+1)]
    sum_of_factorials = 0
    for i in range(len(digits)):
        sum_of_factorials += factorial(digits[i])

    if sum_of_factorials == n+1:
        values.append(n+1)

answer = sum(values)-3
print(answer)
