def p(n):
    return int(n*(3*n-1)/2)

def isPent(Pn):
    x = 6*Pn
    if x/int(x**0.5) == int(x**0.5)+1:
        return True
    return False

pentagonals = []
for n in range(1, 3000):
    pentagonals.append(p(n))

D = 9999999999999999       
for Pj in pentagonals:
    for Pk in pentagonals:
        difference = abs(Pk-Pj)
        if (Pj+Pk) in pentagonals and difference in pentagonals and difference < D:
            D = difference

    

