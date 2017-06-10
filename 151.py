from random import choice as  rand_choice
import time

def p63():
    count = 0
    for base in range(1,10):
        for power in range(22):
            x = base**power
            if len(str(x)) == power:
                count += 1
    return count


def reverse(n):
    return int(str(n)[::-1])




def p145():
    rev_numbers = []
    for n in range(10**3):
        x = n+reverse(n)

        count = 0
        for char in str(x):
            if int(char) % 2:
                count += 1
                
        if count == len(str(x)) and n%10 != 0:
            rev_numbers.append(n)

    print(rev_numbers)
    return len(rev_numbers)


def p151():
    pass




#4.338098
#4.338097699769977
def checkEqual(lst):
       return lst[1:] == lst[:-1]

def run():
    #print("Initializing global iteration {}...".format(global_iterations))
    print("Calculating global iteration {}...".format(global_iterations))
    mainstart = time.time()
    start = time.time()

    def new_envelope():
        for k in spare:
            spare[k] += 1

    spare = {"A2": 0, "A3": 0, "A4": 0, "A5": 0}
    weeks =  10000000 #iterations - the more, the more accurate
    counts = [int(0) for x in range(weeks)]
    sum_expectance = 0
    week = 0 #iterations

    #print("Initializing complete.\n\nCalculating...")

    for week in range(1, weeks):
        #FIRST
        new_envelope()
       

        #MIDDLE 14
        for batch in range(14):
           
            key = rand_choice(list(spare))
            while spare[key] == 0:
                key = rand_choice(list(spare))

            spare[key] -= 1
            
            if key == "A2":
                spare["A3"] += 1
                spare["A4"] += 1
                spare["A5"] += 1
                
            if key == "A3":
                spare["A4"] += 1
                spare["A5"] += 1
                
            if key == "A4":
                spare["A5"] += 1

        
            if spare["A2"] == 0 and spare["A3"] == 0 and spare["A4"] == 0:
                counts[week] += 1
        
            elif spare["A2"] == 0 and spare["A3"] == 0 and spare["A5"] == 0:
                counts[week] += 1
                
            elif spare["A2"] == 0 and spare["A4"] == 0 and spare["A5"] == 0:
                counts[week] += 1
                
            elif spare["A3"] == 0 and spare["A4"] == 0 and spare["A5"] == 0:
                counts[week] += 1

        #LAST
        key = rand_choice(list(spare))
        while spare[key] == 0:
            key = rand_choice(list(spare))

        spare[key] -= 1

        #if not week % 1000:
    expectance = sum(counts)/week
            #print(round(expectance,6))


    #print("\nExpectance: {}\nRounded Expectance: {}".format(expectance, round(expectance,6)))
    print("Rounded Expectance: {}".format(round(expectance,6)))
    
    mainend = time.time()
    print("Time taken for {} iterations: {} seconds".format(weeks, round(mainend-mainstart,2)))
    print("Total Iterations: {}\n".format(weeks*global_iterations))



    return expectance

last10 = []
global_iterations = 0
all_iterations = []

while True:
    global_iterations += 1
    local_ex = run()
    
    if len(last10) == 10:
        del last10[0]

        if checkEqual(last10) == True:
            break
        
    all_iterations.append(local_ex)
    global_expectance = sum(all_iterations)/global_iterations
    last10.append(round(global_expectance,6))
    print("Last 10:",last10)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nIMPROVING EXPECTANCE: {}\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n".format(round(global_expectance,6)))


    
answer = last10[-1]
print(answer)
