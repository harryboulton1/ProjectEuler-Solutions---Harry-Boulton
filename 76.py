n = 10

combinations = []
digits = []
for d in range(n):
    digits.append(1)

while True:
    print(digits)
    combinations.append(digits)
    digits = sorted(digits)

    if digits == digits[::-1]:
        new = digits[0]+1
        del digits[0]
        digits.append(new)
    else:
        while sum(digits) < n:
            smallest1, smallest2 = digits[0], digits[1]    
            del digits[0]
            del digits[0]

            digits.append(smallest1+smallest2)
