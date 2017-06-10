count = 2
nth_prime = 1

while True:
    isprime = True
    
    for x in range(2, int(count**0.5 + 1)):
        if count % x == 0: 
            isprime = False
            break
    
    if isprime:
        #print(count)
        #print(nth_prime)
        nth_prime += 1
    else:
        pass

    if nth_prime > 10001:
        answer = count
        break

    
    count += 1
    
print(answer)
