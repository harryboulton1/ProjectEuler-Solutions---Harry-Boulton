def fct(n):
    x = 1
    for i in range(n):
        x *= i+1
    return x

def c(n,r):
    if type(n) != int or type(r) != int:
        print("n and r must be integers")
    else:
        return int(fct(n) / (fct(r)*fct(n-r)))

count = 0
for n in range(1,101):
    for r in range(n):
        if c(n,r) > 1000000:
            count += 1

print(count)
