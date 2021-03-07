import math

listOfPrimes = []
def primeChecker(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primeSummation(upperBound):
    for i in range(2, upperBound):
        if primeChecker(i) == True:
            listOfPrimes.append(i)
        else:
            continue
    return sum(listOfPrimes)

print(primeSummation(2000000))



