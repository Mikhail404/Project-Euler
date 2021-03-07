#the challenge with this question is trying to wrap your head around the double negative as it can lead you to losing your
#train of thought if you're not careful

#simply put, you want to make a function that returns TRUE if and only if the result of dividing a counter variable by an
#iterator is 0, but for all numbers. This little trick is done by placing 'return True' outside of the functions thereby
#'forcing' it to work the intended way. It's much easier this way because you don't have to check for every single number
#between 1 and 20, instead you just make it return True if it finds an 'n' that accepts all 'i's as even when divided (n%i)
#if it doesnt, we increment n and keep on searching. Really straight forward once you figure to use the 'return True' outside.



def divisibleChecker(n):
    #search between 1 and 20. Although technically you could save maybe 1/100th of 1ms if you did (2, 21)
    for i in range(1, 21):
        #if n divided by i does not equal 0, return False and increment n so we can keep on searching for a valid n
        if n % i != 0:
            return False
    #however, if n divided by i does in fact yield 0 (this is of course for all 1-20 and NOT per iteration of the for loop
    #because we are now outside of the loop and the computer understands this as the for loop being completed)
    #then just return True which will take us to line 25 which takes us to line 26 which breaks and tells the program to
    #print the 'n' that it found which accepts all 'i's as even when divided (n%i)
    return True


n = 1
while True:
    if divisibleChecker(n):
        break
    else:
        n += 1

print(n)