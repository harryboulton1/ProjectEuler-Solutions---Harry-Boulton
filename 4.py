def palindrome_check(n):
    n_split = [int(i) for i in str(n)]
    
    for i in range(len(n_split)):
        if n_split[i] == n_split[-i-1]:
            pass
        else:
            return False
    return True

palindromes = []
for a in range(100, 1000):
    for b in range(100, 1000):

        n=a*b

        if palindrome_check(n):
            palindromes.append(n)

palindromes = sorted(palindromes)
answer = palindromes[-1]

print(answer)
