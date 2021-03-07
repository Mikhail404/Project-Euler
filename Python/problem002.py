
def fibonacci(n):

    #create a list to hold regular fibonacci terms, starting with 1 and 2 because we obviously need a starting point
    fibonacci_list = [1, 2]
    #create a new list to hold only the even fibonacci terms, starting with 2
    even_fibonacci_list = [2]


    for i in range(2, n):
        #gets the number immediately to the left of the number to be calculated + the number 2 spaces to the left
        nextNumber=fibonacci_list[i-1] + fibonacci_list[i-2]
        #adds that number to our regular fibonacci list
        fibonacci_list.append(nextNumber)

        #lines 17-27 simply check if the number is even, if it is then it appends it to the even fibonacci list
        #we then sum our terms inside of that even fibonacci list
        #if that value is less than 4 million, we print it, else we break.
        if nextNumber%2==0:
            even_fibonacci_list.append(nextNumber)
        
        sum_of_even_terms = sum(even_fibonacci_list)

        if sum_of_even_terms<=4000000:
            print(sum_of_even_terms)
        else:
            break

    return sum_of_even_terms

print(fibonacci(1000))



    ####### ALTERNATIVE WAY - REPLACES LINES 19-27 INCLUSIVE #######
        # count = 0
        # for number in even_fibonacci_list:            
        #     if count>=4000000:
        #         break
        #     count += number



####### older versions, if you can think of a way to fix them, let me know #######
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