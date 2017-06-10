def isInteger(n):
    if n % 2 == 0 or (n+1) % 2 == 0:
        return True
    return False


def create_dictionary(r):
    dic = {}
    for i in range(r):
        dic[i+1] = 0
    return dic

def local_solutions(perimeter):
    solutions = []
    for a in range(1, perimeter):
        for b in range(1, perimeter):
            c = (a**2+b**2)**0.5
            
            if isInteger(c) == True:
                c = int(c)
                p = a+b+c
                
                if p == perimeter:
                    p_list = [a, b, c]
                    solutions.append(p_list)

                    for lis in solutions:
                        for side in lis:
                            for lis1 in solutions:
                                if side == lis[0] and side == lis1[1]:
                                    solutions.remove(lis)             
    return len(solutions)


r = 1000

print("Generating Dictionary...")
solutions = create_dictionary(r)
print("Dictionary Generated!\n")

for perim in range(r):
    perim = perim+1
    print("Working solutions for perimeter = "+str(perim))
    solutions[perim] = local_solutions(perim)


answer = max(solutions, key=solutions.get)
print(answer)
