def sum_of_multiples(n):
    
    return sum(num for num in range(n) if num%3==0 or num%5==0)
    

print(sum_of_multiples(1000))
