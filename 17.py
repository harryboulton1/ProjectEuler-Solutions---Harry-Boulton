
#1-9:    9/ten
#        81/hundred 
#        810/thousand
#        90 of each number as a unit

#Teens:
#        9/hundred
#        90/thousand
#        9 of each number as a unit

#Multiples of Ten: 
#        10/hundred
#        100/thousand

#Ands:   99/hundred*
#        891 TOTAL

#Hundreds 899 TOTAL

cum_list = []
n1 = len("one")
n2 = len("two")
n3 = len("three")
n4 = len("four")
n5 = len("five")
n6 = len("six")
n7 = len("seven")
n8 = len("eight")
n9 = len("nine")

n10 = len("ten")
n11 = len("eleven")
n12 = len("twelve")
n13 = len("thirteen")
n14 = len("fourteen")
n15 = len("fifteen")
n16 = len("sixteen")
n17 = len("seventeen")
n18 = len("eighteen")
n19 = len("nineteen")

n20 = len("twenty")
n30 = len("thirty")
n40 = len("forty")
n50 = len("fifty")
n60 = len("sixty")
n70 = len("seventy")
n80 = len("eighty")
n90 = len("ninety")

n100 = len("hundred")
n1000 = len("thousand")

n_and = len("and")

cum_list.append((n1*100)+(n2*99)+(n3*99)+(n4*99)+(n5*99)+(n6*99)+(n7*99)+(n8*99)+(n9*99))
cum_list.append((n10*10)+(n11*10)+(n12*10)+(n13*10)+(n14*10)+(n15*10)+(n16*10)+(n17*10)+(n18*10)+(n19*10))
cum_list.append((n20*10)+(n30*10)+(n40*10)+(n50*10)+(n60*10)+(n70*10)+(n80*10)+(n90*10))
cum_list.append(n_and*891)
cum_list.append(n100*899)
cum_list.append(n1000)

lens = sum(cum_list)
print(cum_list)
print(lens)
