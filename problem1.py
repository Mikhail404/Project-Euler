def sum_of_multiples(n):
    
    list_of_nums_to_sum = []

    for num in range(n):
        if num%3==0 or num%5==0:
            list_of_nums_to_sum.append(num)
    
    Sum = sum(list_of_nums_to_sum)
    print(Sum)
    return None

print(sum_of_multiples(1000))






