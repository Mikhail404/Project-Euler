def powerDigitSum(n):

    digitStr = str(int(n**1000))  #replace '1000' with the power
    someList = []

    for _ in digitStr:
        someList.append(int(_))

    Sum = sum(someList)
    return Sum

print(powerDigitSum(2))