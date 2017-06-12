def fct(n):
    x=1
    for m in range(1,n+1): x*=m
    return x

def C(n, r):
    return int(fct(n)/(fct(r)*fct(n-r)))

n = 20 #x
k = 20 #y
paths = C((n+k),n)

print(paths)
