def palindrome_product(lowerbound, upperbound):
    
    return max(i*j for i in range(upperbound, lowerbound, -1) for j in range(upperbound, lowerbound, -1) if isPalindrome(i*j))






def isPalindrome(n):

    return str(n)==str(n)[::-1]







print(palindrome_product(100, 999))