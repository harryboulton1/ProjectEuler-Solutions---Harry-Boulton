import time

start = time.time()

def evaluate(n):
    n=str(n)
    if n[0]==1 and n[2]==2 and n[4]==3 and n[6]==4 and n[8]==5 and n[10]==6 and n[12]==7 and n[14]==8 and n[16]==9 and n[18]==0:
        return True

for i in range(1010101010, 1389026624, 10):
    if evaluate(i**2):
        break

end = time.time()

print(i)
print(end-start)
