
#1 - Multiples of 3 and 5
def p1():
    numbers = []
    for i in range(1000):
        if i % 3 == 0:
            numbers.append(i)
        elif i % 5 == 0:
            numbers.append(i)

    answer = sum(numbers)
    return answer

#2 - Even Fibonacci Numbers

def p2():

    final_terms = []

    a = 1
    b = 2

    for i in range(100):
        i=i
        if a < 4000000 and a % 2 == 0:
                final_terms.append(a)
        if b < 4000000 and b % 2 == 0:
                final_terms.append(b)
        a = a + b
        b = a + b

    answer = sum(final_terms)
    return answer

#3 - Largest Prime Factor
def p3():
    def pfs(n):
        factors = []
        prime_factors = []
        for i in range(n):
            d = i+1
            if n % d == 0 and d not in factors:
                factors.append(d)

        for i in range(len(factors)):
            factors2 = []
            for k in range(factors[i]):
                d = k+1
                if factors[i] % d == 0:
                    factors2.append(d)

                    
            if len(factors2) == 2 and factors2[1] not in prime_factors:
                prime_factors.append(factors2[1])

        return prime_factors
            
    answer = pfs(600851475143)
    return answer
#4 - Largest Palindrome Product
def p4():
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
    return answer


#5 - Smallest Multiple
def p5():
    def divide(n):
        count = 0
        for i in range(20):
            divisor = i+1
            if n % divisor == 0:
                count += 1
                if count == 20:
                    return True
            else:
                count = 0

    n = 0
    while True:
        n += 1
        if divide(n):
            break

    answer = n
    return answer

#6 - Sum Square Difference
def p6():
    sum_of_squares = 0
    sumx = 0

    for i in range(100):
        n = i+1
        sum_of_squares += n**2

    for i in range(100):
        n = i+1
        sumx += n

    square_of_sum = sumx**2

        
    answer = square_of_sum - sum_of_squares
    return answer




#7 - 10001st Prime
def p7():
    import math

    count = 2
    nth_prime = 1
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            #print(count)
            #print(nth_prime)
            nth_prime += 1
        else:
            pass

        if nth_prime > 10001:
            answer = count
            break

        
        count += 1
        
    return answer



#8 - Largest Product in a Series
def p8():
    number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    number = [int(i) for i in str(number)]
    products = []

    for pointer in range(1000-12):
        thirteen_digits = []
        
        for i in range(13):
            thirteen_digits.append(number[i+pointer])
            
            product = 1
            for x in thirteen_digits:
                product *= x
        products.append(product)

    products = sorted(products)
    answer = products[-1]

    return answer
#9 - Special Pythagorean Triplet
def p9():
    a, b, c = 0, 0, 0

    for a in range(333):                #For speed, set range to (198,202)
        for b in range(1000):
            for c in range(1000):
                if (a < b) and (b < c) and (a**2 + b**2 == c**2) and a+b+c == 1000:
                    answer = a*b*c
    return answer


#10 - Summation of Primes

def p10():
    import math
        
    count = 2
    primes = []

    while count < 2000000:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            primes.append(count)
        else:
            pass
        
        count += 1

    answer = sum(primes)
    return answer



#11 - Largest Product in a Grid

def p11():
    def create_rows():
        global rows
        rows = [[8,  2,  22, 97, 38, 15, 0,  40, 0,  75, 4,  5,  7,  78, 52, 12, 50, 77, 91, 8],
                [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4,  56, 62, 0],
                [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3,  49, 13, 36, 65],
                [52, 70, 95, 23, 4,  60, 11, 42, 69, 24, 68, 56, 1,  32, 56, 71, 37, 2,  36, 91],
                [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
                [24, 47, 32, 60, 99, 3,  45, 2,  44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
                [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
                [67, 26, 20, 68, 2,  62, 12, 20, 95, 63, 94, 39, 63, 8,  40, 91, 66, 49, 94, 21],
                [24, 55, 58, 5,  66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
                [21, 36, 23, 9,  75, 0,  76, 44, 20, 45, 35, 14, 0,  61, 33, 97, 34, 31, 33, 95],
                [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3,  80, 4,  62, 16, 14, 9,  53, 56, 92],
                [16, 39, 5,  42, 96, 35, 31, 47, 55, 58, 88, 24, 0,  17, 54, 24, 36, 29, 85, 57],
                [86, 56, 0,  48, 35, 71, 89, 7,  5,  44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
                [19, 80, 81, 68, 5,  94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4,  89, 55, 40],
                [4,  52, 8,  83, 97, 35, 99, 16, 7,  97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
                [88, 36, 68, 87, 57, 62, 20, 72, 3,  46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
                [4,  42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8,  46, 29, 32, 40, 62, 76, 36],
                [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4,  36, 16],
                [20, 73, 35, 29, 78, 31, 90, 1,  74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5,  54],
                [1,  70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1,  89, 19, 67, 48]]


    def create_columns():
        global columns
        columns = []
        
        for i in range(20):
            column = []
            for ii in range(20):
                column.append(rows[ii][i])
            columns.append(column)

    def create_diagonals():
        global diagonals
        diagonals = []

        def create_desc_diagonals():
            desc_diagonals = []
            
            for yshift in range(20):
                
                for xshift in range(20):
                    diagonal = []
                    
                    for i in range(4):
                        start = i+1
                        number = find(start+xshift,start+yshift)
                        diagonal.append(number)
                        
                    desc_diagonals.append(diagonal)
                    
            return desc_diagonals

        def create_asc_diagonals():
            asc_diagonals = []
            
            for yshift in range(20):
                
                for xshift in range(20):
                    diagonal = []       
                    for i in range(4):
                        xstart = i+1
                        ystart = 1-i
                        number = find(xstart+xshift,ystart+yshift)      
                        diagonal.append(number)
                        
                    asc_diagonals.append(diagonal)

            return asc_diagonals

        diagonals.extend(create_desc_diagonals())
        diagonals.extend(create_asc_diagonals())

        create_desc_diagonals()
        create_asc_diagonals()

        return diagonals
        
    def find(x, y):
        if 21 > x > 0 and 21 > y > 0:
            value = columns[x-1][y-1]
            return value
        else:
            return 0


    def find_LR_products():
        LR_products = []
        for row in range(len(rows)):
            for pointer in range(20-3):
                    four_digits = []
                    
                    for i in range(4):
                        four_digits.append(rows[row-1][i+pointer])

                        product = 1
                        for x in four_digits:
                            product *= x
                    LR_products.append(product)
                    
        return LR_products

    def find_UD_products():
        UD_products = []
        for column in range(len(columns)):
            for pointer in range(20-3):
                    four_digits = []
                    
                    for i in range(4):
                        four_digits.append(columns[column-1][i+pointer])

                        product = 1
                        for x in four_digits:
                            product *= x
                    UD_products.append(product)
                    
        return UD_products


    def find_DG_products():
        DG_products = []
        diagonals = create_diagonals()

        product = 1
        for item in diagonals:

            product = 1
            for x in item:
                product *= x
            DG_products.append(product)

        return DG_products


    create_rows()
    create_columns()
    create_diagonals()

    all_products = []
    all_products.extend(find_LR_products())
    all_products.extend(find_UD_products())
    all_products.extend(find_DG_products())
    all_products = sorted(all_products)
    answer = all_products[-1]
    
    return answer

#13 Large Sum


def p12():
    
    n, t= 0,0

    factors = []
    while len(factors) < 500:
        n += 1
        t += n
    
        factors = []
        for divisor in range(1, int((t**0.5)+1)):
            if t % divisor == 0 and divisor not in factors:
                factors.append(divisor)
                factors.append(int(t/divisor))
    
    return t

def p13():
    n = 37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690
    n_list = [int(x) for x in str(n)]

    numbers = []
    for num in range(100):
        number = []
        for digit in range(50):
            number.append(n_list[50*num+digit])
    
            number = int("".join(map(str, number)))
            numbers.append(number)

            sum_list = [int(x) for x in str(sum(numbers))]
            first_ten_digits_list = []

    for i in range(10):
        nth_sum_digit = sum_list[i]
        first_ten_digits_list.append(nth_sum_digit)
    
        first_ten_digits = int("".join(map(str, first_ten_digits_list)))
        print(first_ten_digits)
    
#14 - Longest Collatz Sequence
def p14():
    def evaluate_length(n):
    
        count = 1
        while n != 1:
            if n % 2 == 0:
                n = int(n/2)
            else:
                n = int(3*n + 1)
    
            count += 1
        return count

    lengths = {}
    for n in range(1,1000000):
        lengths[n] = (evaluate_length(n))
    
    lengths_sorted = sorted(lengths.values())
    longest = lengths_sorted[-1]

    for x in lengths.keys():
        if lengths[x] == longest:
            return x

def p17():

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

#16 Large Power Sum
def p16():
    return sum([int(x) for x in str(2**1000)])


def p20():
    def factorial(n):
        x = 1
        for i in range(n):
            x *= n-i
        return x
        
    return sum([int(x) for x in str(factorial(100))])



def p21():

    def find_divisors(n):
        divisors = []
       
        for d in range(1, int(n**0.5+1)):
            if n % d == 0 and n!= d and d not in divisors:
                divisors.append(d)
                divisors.append(int(n/d))
    
        divisors.remove(n) #n is a divisor, but only divisors < n are wanted
        return divisors


    def d(n):
        return sum(find_divisors(n))

    amicables = []

    for a in range(2, 10000):
        for b in range(2, 10000):


            if d(a) == b and d(b) == a and a != b:
                #isAmicable = True
                if d(a) not in amicables:
                    amicables.append(a)
                if d(b) not in amicables:
                    amicables.append(a)
    #print(amicables)

    return sum(amicables)


def p22():
    alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    names = open("names.txt", "r")
    names = names.readline()
    names = names.replace('"', "")
    names = names.split(",")
    names = sorted(names)

    def value(name):
        value = 0
        for char in list(name): #for each character in name
            value += alphabet[char.lower()]
        return value

    position = 0
    total = 0

    for name in names: #for each name
        position += 1
        score = value(name)*position
    
        total += score
    
    
    return total
    

def p23():
    upperbound = 28124 #28124

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
                #print(len(newlist))
        return newlist


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

    def diff(first, second):
            second = set(second)
            return [item for item in first if item not in second]

    answer = sum(diff(all_ints, abundant_sum))
    return answer

##    import sys
##    f = open("file.txt", "w")
##    f.write(str(answer))
##    f.close()
##    4 HOURS

    
def p28():
    def generate_spiral(size):
        grid = [([0 for columns in range(size)]) for rows in range(size)]       
        return grid

    size = 5
    spiral = generate_spiral(size)
    
    c = int(size/2 + 1)
    start = spiral[c][c]
    
    
    def next_shift(shift):
        if shift > 0:
            shift = -1*(shift+1)
        elif shift < 0:
            shift = -1*(shift-1)
        return shift


def p29():

    LB = 2
    UB = 100

    terms = []
    for base in range (LB, UB+1):
        for power in range(LB, UB+1):
            x = base**power
            if x not in terms:
                terms.append(x)

    return len(terms)

def p30():
    power = 5
    def list_int(n):
        return [int(x) for x in str(n)]

    def sum_powered_digits(n_list):
        total = 0
        for digit in n_list:
            total += digit**power
        return total

    correct = []
    for n in range(1000000):
        if sum_powered_digits(list_int(n)) == n:
            correct.append(n)

    return sum(correct)-1


def p34():

    r = 100000

    def factorial(n):
        x = 1
        for i in range(n):
            x *= i+1
        return x
            
    values = []
    for n in range(r):
        digits = [int(x) for x in str(n+1)]
        sum_of_factorials = 0
        for i in range(len(digits)):
            sum_of_factorials += factorial(digits[i])

        if sum_of_factorials == n+1:
            values.append(n+1)

    return sum(values)-3

#P35

def p35():

    r = 1000000

    def rotate(n):
        n_list = [int(x) for x in str(n)]
        rotations = []
        for digit in range(len(str(n))):
            rotations.append(int(''.join(map(str,n_list))))
            n_list.append(n_list.pop(0))
            
        return rotations


    def gen_primes(n):
        size = n//2
        sieve = [1]*size
        limit = int(n**0.5)
        for i in range(1,limit):
            if sieve[i]:
                val = 2*i+1
                tmp = ((size-1) - i)//val 
                sieve[i+val::val] = [0]*tmp
        return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

    print("Generating primes below {}...".format(r))
    primes = gen_primes(r)
    print("Primes generated...")
    circular_primes = []

    print()
    print("Calculating circular primes below {}...".format(r))
    for prime in primes:
        rotations = rotate(prime)
        primes_in_rotations = 0
        for i in rotations:
            if i not in primes:
                break
            else:
                primes_in_rotations += 1

            if primes_in_rotations == len(rotations) and prime not in circular_primes:
                circular_primes.append(prime)
                print("{} added!".format(str(prime)))

    print("Complete! There are {} circular primes below {}".format(str(len(circular_primes)), str(r)))
    return len(circular_primes)


def p36():

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

    return sum(palindromes)

def p39():

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


    return max(solutions, key=solutions.get)

def p43():
    import itertools
    permutations = [list(i) for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9])]

    primes = [2,3,5,7,11,13,17]
    def concat(digits, i):
        return int(str(digits[i+1])+str(digits[i+2])+str(digits[i+3]))

    solutions = []
    for n in permutations:
        digits = {}
        for digit in n:
            digits[digit+1] = n[digit]


        count = 0
        for i in range(1,8):
            #print(i+1, i+2, i+3)
            #print(primes[i-1])
            triplet = concat(digits,i)
            if triplet % primes[i-1] == 0:
                count += 1
            #if int("".join(digits[i+1],digits[i+2],digits[i+3])) % primes[i-1] == 0:
            #    count += 1
                #print(count)

        if count == 7:
            solution = int(''.join(str(i) for i in n))
            solutions.append(solution)

    return sum(solutions)


def p48():
    total = 0
    for i in range(1,1000+1):
        total += i**i
    return total

def p52():
    
    def f(x):
        return sorted([int(i) for i in str(x)])
    
    x=0
    while True:
        x+=1
        if f(x) == f(2*x) == f(3*x) == f(4*x) == f(5*x) == f(6*x):
            return x


def p53():
    def fct(n):
        x = 1
        for i in range(n):
            x *= i+1
        return x

    def c(n,r):
        if type(n) != int or type(r) != int:
            print("n and r must be integers")
        else:
            return int(fct(n) / (fct(r)*fct(n-r)))

    count = 0
    for n in range(1,101):
        for r in range(n):
            if c(n,r) > 1000000:
                count += 1

    return count


def p55():
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
                

    return lychrels

