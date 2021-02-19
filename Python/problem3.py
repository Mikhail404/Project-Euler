#To find the largest prime factor, we first need the smallest prime factor(s). we divide our input by this 
#until we cannot divide any further.

#in other words, we take our input 'n' and keep on dividing it by its smallest prime factor, if we then take
#the final prime factor that divides into n, we will have the largest value, more succinctly, we will have 
#the largest prime factor.
import math

def smallest_prime_factor(n):
    #by mathematical definition, the smallest prime number is 2 as it is only divisible by 1 and itself, 2.
    #so, we need to first eliminate this case
    if n%2==0:      #if 2 divides evenly into n
        return 2    #return 2

    #iterate from i=3 to sqrt(n)
    #if a number along the loop divides into n, it MUST be the smallest prime factor
    #if none divide, then n itself is the smallest prime factor
    i=3
    while math.sqrt(i)<=n:
        if n%i==0:
            return i
        i = i + 2
    return n


def largest_prime_factor(n):
    #this will loop the body of this code indefinitely, we need to do this because we want to keep on dividing through n
    #until we can find the largest prime factor
    while True:
        #calling our above function on n, stored in a new variable 'smallest_factor'
        smallest_factor = smallest_prime_factor(n)

        #if this number is less than n, update n to contain the division of the two
        if smallest_factor<n:
            n = n // smallest_factor
        else:
            #otherwise it must be n itself, in which case return n.
            return n

result = 600851475143
print("largest prime factor of", result, "is", largest_prime_factor(result))