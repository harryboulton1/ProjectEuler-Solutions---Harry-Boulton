def f(x):
    return sorted([int(i) for i in str(x)])

x=0
while True:
    x+=1
    if f(x) == f(2*x) == f(3*x) == f(4*x) == f(5*x) == f(6*x):
        break

print(x)
