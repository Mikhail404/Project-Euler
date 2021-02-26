def sumOfSquares(n):
    return sum(i*i for i in range(0, n+1))
    

def squareOfSums(n):
    a = sum(i for i in range(0, n+1))
    return a*a
    

def difference(n):
    return squareOfSums(n) - sumOfSquares(n)


print(difference(100))
