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
