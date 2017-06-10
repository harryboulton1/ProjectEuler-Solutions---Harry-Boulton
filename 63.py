count = 0
for base in range(1,10):
    for power in range(22):
        x = base**power
        if len(str(x)) == power:
            count += 1
print(count)
