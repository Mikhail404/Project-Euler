def palindrome_product(lowerbound, upperbound):
    return max(i*j for i in range(upperbound, lowerbound, -1) for j in range(upperbound, lowerbound, -1) if isPalindrome(i*j))


def isPalindrome(n):
    #returns the reversed string to be compared in line 8 which acts as a pseudo 'check'
    return str(n)==str(n)[::-1]


print(palindrome_product(100, 999))