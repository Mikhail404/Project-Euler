def sumOfSquares(n):
    squares_list = []
    numbers_list = []

    for i in range(0, n+1):
        square = i*i
        squares_list.append(square)
    Sum = sum(squares_list)
    print(Sum)


    for i in range(0, n+1):
        numbers_list.append(i)
    Sum2 = sum(numbers_list)
    squareOfSums = Sum2*Sum2
    print(squareOfSums - Sum)


sumOfSquares(100)

    








