def divisibleChecker(n):

    if all(i for i in range(1, 21) if n % i != 0):
        pass

        

n = 1
while True:
    if divisibleChecker(n):
        break
    else:
        n += 1

print(n)