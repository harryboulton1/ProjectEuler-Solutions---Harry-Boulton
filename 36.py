def isPalindrome(n):
    n_split = [int(i) for i in str(n)]
    for i in range(len(n_split)):
        if n_split[i] == n_split[-i-1]:
            pass
        else:
            return False
    return True

def binary(n):

    binary_list = []
    def largestPowerOf2(n):
        p = 0
        while True:
            p+=1
            if 2**p > n:
                return p
  
    largestPower = largestPowerOf2(n)
    for p in range(largestPower):
        q = largestPower - p-1
        if n >= 2**q:
            binary_list.append(1)
            n = n-2**q
        else:
            binary_list.append(0)
    
    return int("".join(str(x) for x in binary_list))


palindromes = []
r = 1000000
for i in range(r):
    if isPalindrome(i) == True and isPalindrome(binary(i)) == True:
        palindromes.append(i)
        pass

answer = sum(palindromes)
print(answer)
