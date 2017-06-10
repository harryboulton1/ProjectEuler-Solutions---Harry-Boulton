def divide(n):
    count = 0
    for i in range(20):
        divisor = i+1
        if n % divisor == 0:
            count += 1
            if count == 20:
                return True
        else:
            count = 0

n = 0
while True:
    n += 1
    if divide(n):
        break

answer = n

print(answer)
