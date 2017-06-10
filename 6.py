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

print(answer)
