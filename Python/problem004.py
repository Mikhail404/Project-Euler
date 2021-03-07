def palindrome_product(lowerbound, upperbound):
    #initialise variable to hold the current max number
    cur_max = 0
    #iterate through all numbers for both loops from the upperbound to the lowerbound
    #this way, the first occurrence of a palindrome will also be the highest
    for i in range(upperbound, lowerbound, -1):
        for j in range(upperbound, lowerbound, -1):
            if isPalindrome(i*j):   #if the product of i and j is a palindrome, check if its the highest number
                if i*j>cur_max:     #if the resulting product is greater than max
                    cur_max = i*j   #set the max equal to the product of the 2 variables i,j
    return cur_max



####### replace lines 3-11 for a more concise version using generator expressions #######
#this returns the product of i,j to max for comparison so it can determine which product is actually the max
#and then simply combines the entire body of the code into 1 clean line which finally checks against the isPalindrome function

#note: this code on its own will not run properly until you replace lines 3-11 since line 20 is just a condensed version of that
    #return max(i*j for i in range(upperbound, lowerbound, -1) for j in range(upperbound, lowerbound, -1) if isPalindrome(i*j))



def isPalindrome(n):
    #returns the reversed string to be compared in line 8 which acts as a pseudo 'check'
    return str(n)==str(n)[::-1]


print(palindrome_product(100, 999))
