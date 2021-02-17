def sum_of_multiples(n):

    #create a new list to hold our numbers so we can sum them later
    list_of_nums_to_sum = []
    
    #iterates over n, if the value when divided by 3 or 5 = 0, then we add it to a list
    #sum up everything in that list 
    for num in range(n):
        if num%3==0 or num%5==0:
            list_of_nums_to_sum.append(num)
    
    Sum = sum(list_of_nums_to_sum)
    print(Sum)
    return None

print(sum_of_multiples(1000))
