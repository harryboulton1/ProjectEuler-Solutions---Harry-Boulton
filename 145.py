def reverse(n):
    return int(str(n)[::-1])

rev_numbers = []
for n in range(10**3):
    x = n+reverse(n)

    count = 0
    for char in str(x):
        if int(char) % 2:
            count += 1
            
    if count == len(str(x)) and n%10 != 0:
        rev_numbers.append(n)

print(rev_numbers)
return len(rev_numbers)
