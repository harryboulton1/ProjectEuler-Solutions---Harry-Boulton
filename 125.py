def isPalindrome(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != n[-i-1]:
            return False
    return True

def largest_square(n):
    for i in range(n,0,-1):
        if str(i**0.5)[-1] == '0':
            return i**0.5

palindromes = []
solutions = []
for i in range(1,10**8):
    if isPalindrome(i):
        palindromes.append(i)
        



for p in palindromes:
    squares = [int(x) for x in range(1, int(largest_square(p)+1))]
    
