def evaluate(n):
    d = list(str(n))
    if d[0]=='1' and d[2]=='2' and d[4]=='3' and d[6]=='4' and d[8]=='5' and d[10]=='6' and d[12]=='7' and d[14]=='8' and d[16]=='9' and d[18]=='0':
        return True
    return False

for i in range(int(1020304050607080900**0.5 + 1), int(1929394959697989990**0.5 + 1)):
    if evaluate(i**2) == True:
        break

print(i)
