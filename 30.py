def list_int(n):
    return [int(x) for x in str(n)]

def sum_powered_digits(n_list):
    total = 0
    for digit in n_list:
        total += digit**power
    return total

power = 5
correct = []

for n in range(1000000):
    if sum_powered_digits(list_int(n)) == n:
        correct.append(n)

answer = sum(correct)-1
print(answer)
