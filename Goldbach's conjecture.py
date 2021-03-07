''' Goldbach's conjecture '''
#Every even integer greater than 2 can be written as the sum of two primes.

def finds_prime_numbers_in_interval_N(N):
    list_number = []

    while N > 1:
        div, count = 2, 0
        while div <= N / 2 and count == 0:
            if N % div == 0:
                count += 1
            div += 1
        if count == 0:
            list_number.append(N)
        N -= 1
    return list_number

interval = int(input('Enter the interval: '))
starting_number = 4

prime_nubers_list = finds_prime_numbers_in_interval_N(10000)
prime_nubers_list.sort()
while starting_number < interval:
    for item in range(len(prime_nubers_list)):
        if item < starting_number:
            sum_temp = prime_nubers_list[item] + prime_nubers_list[item]

            if starting_number == sum_temp and starting_number <= interval:
                print(str(starting_number) + ': ' + str(prime_nubers_list[item]) + '+' + str(prime_nubers_list[item]))
                starting_number += 2
                break
            else:
                base_item = item
                while prime_nubers_list[base_item] < starting_number:
                    while prime_nubers_list[item+1] < starting_number:
                        item = item + 1
                        sum_temp = prime_nubers_list[item] + prime_nubers_list[base_item]
                        if starting_number == sum_temp and starting_number <= interval:
                            print(str(starting_number) + ': ' + str(prime_nubers_list[item]) + '+' + str(prime_nubers_list[base_item]))
                            starting_number += 2
                            break
                    base_item += 1
                    item = base_item
        else:
            break