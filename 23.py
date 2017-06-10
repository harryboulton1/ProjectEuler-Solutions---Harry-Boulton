def find_divisors(n):
    divisors = []
    for d in range(1, int(n**0.5+1)):

        if n % d == 0 and d not in divisors:
            divisors.append(d)
            if int(n/d) not in divisors:
                divisors.append(int(n/d))
                   
    divisors = sorted(divisors)
        
    divisors.remove(n)
    return divisors


def remove_duplicates(lis):
    global newlist
    newlist = []
    count = 0
    for i in lis:
        count += 1
        if i not in newlist:
            newlist.append(i)
    return newlist

def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

upperbound = 28124

abundants = []
for n in range(1, upperbound):
    if sum(find_divisors(n)) > n:
        abundants.append(n)
    
abundant_sum = []
for n1 in abundants:
    for n2 in abundants:
        abundant_sum.append(n1+n2)

abundant_sum = remove_duplicates(abundant_sum)
#x= sum of every abundant number + every other abundant number

all_ints = []
for i in range(1, upperbound):
    all_ints.append(i)

answer = sum(diff(all_ints, abundant_sum))
print(answer)
