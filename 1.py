numbers = []
for i in range(1000):
    if i % 3 == 0:
        numbers.append(i)
    elif i % 5 == 0:
        numbers.append(i)
answer = sum(numbers)

print(answer)
