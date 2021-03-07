def pythagoreanTriplet(upperBound):
    for a in range(1, upperBound):
        for b in range(1, upperBound):
            c = upperBound - a - b
            if a**2 + b**2 == c**2:
                if a<=b<c:
                    return a*b*c
                

upperBound = 1000
print(pythagoreanTriplet(upperBound))