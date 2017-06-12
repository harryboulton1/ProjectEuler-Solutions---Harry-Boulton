def streak(n):
    k=0
    while True:
        k += 1
        if (n+k-1) % (k):
            break
        else:
            pass
    return k-1


def P(s, N):
    count = 0
    for n in range(2, N):
        if streak(n) == s:
            count += 1
    return count

total = 0
for i in range(1,32):
    total += P(i,4**i)      #total for 1,17 = 8196
    print(i)                # i.e 1-16
    print(total)
