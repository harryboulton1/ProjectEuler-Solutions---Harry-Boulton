def factorial(n):
    x = 1
    for i in range(n):
        x *= n-i
    return x
    
answer = sum([int(x) for x in str(factorial(100))])
print(answer)
