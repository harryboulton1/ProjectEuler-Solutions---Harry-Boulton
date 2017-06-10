def isPalindrome(n):
    n_split = [int(i) for i in str(n)]
    for i in range(len(n_split)):
        if n_split[i] == n_split[-i-1]:
            pass
        else:
            return False
    return True   

def reverse(n):
    n_list = [int(x) for x in str(n)]
    r_list = []
    for i in range(len(n_list)):
        r_list.append(n_list[len(n_list)-i-1])
    r = "".join(str(d) for d in r_list)


    return int(r)

def isLychrel(n):
    if isPalindrome(n+reverse(n)) == True:
        return False
    return True

lychrels = 0
for n in range(10000):

    for i in range(50):

        if isLychrel(n) == False:
            break
        else:
            n = n+reverse(n)
        if i == 49:
            lychrels += 1
            

print(lychrels)
