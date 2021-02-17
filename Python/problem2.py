# def evenFibonacci(n):

#     result_list = [1, 2]

#     for i in range(2, n):
#         if num%2==0:
#             result_list.append(result_list[num-1]+result_list[num-2])


#     return result_list


# print(evenFibonacci(10))



# def fibonacci(n):

#     fibonacci_list = [1, 2]
#     even_fibonacci_list = [2]

#     for i in range(2, n):
#         nextNumber=fibonacci_list[i-1] + fibonacci_list[i-2]
#         fibonacci_list.append(nextNumber)

#         # if nextNumber%2==0:
#         #     even_fibonacci_list.append(nextNumber)
    
#     return fibonacci_list


# print(fibonacci(400))



def fibonacci(n):

    fibonacci_list = [1, 2]
    even_fibonacci_list = [2]

    for i in range(2, n):
        nextNumber=fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(nextNumber)

        if nextNumber%2==0:
            even_fibonacci_list.append(nextNumber)
        
        sum_of_even_terms = sum(even_fibonacci_list)

        if sum_of_even_terms<=4000000:
            print(sum_of_even_terms)
        else:
            break

    return sum_of_even_terms

print(fibonacci(1000))




        # count = 0
        # for number in even_fibonacci_list:            
        #     if count>=4000000:
        #         break
        #     count += number



        