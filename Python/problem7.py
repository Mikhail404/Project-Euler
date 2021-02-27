#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
def primeChecker(n):
    #checks from 2 to right before the specified number
    #if that number gets divided evenly by all of the numbers before it (from 2 to that number-1)
    #then it must be a prime
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def whatNumberIsThatPrime(n):
    nthPrime = 0    #tracks what number prime its up to
    primeNumber = 0 #tracks the prime number itself

    #we loop over both trackers, increment the prime number by 1 and then check if primeNumber is a prime or not
    #if it is, increment nthPrime so that we know what number prime that prime number is.
    #(i.e, 7 is the 17th prime number, therefore at that instance in the loop, nthPrime = 17 and primeNumber = 7)
    while nthPrime < n:
        primeNumber += 1
        if primeChecker(primeNumber):
            nthPrime += 1
    return primeNumber


        
print(whatNumberIsThatPrime(10001))





    