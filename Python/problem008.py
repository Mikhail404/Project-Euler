numbers = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
def biggestProduct(numbers, lengthOfAdjacent):
    #getting the length of the 1000 digits
    n = len(numbers)
    #counter variable to keep track of the current number
    currentNum = 0
    #loop through the 1000 digits
    for number in range(0, n+1):
        #create a 'segment' out of the 1000 digits that works between the current iteration and the specified length
        #in this case, in chunks of 13 at a time or whatever 'lengthOfAdjacent' you specify in the function call
        segment = numbers[number:number+lengthOfAdjacent]
        #counter variable to keep track of the current product
        currentProduct = 1
        #loop through this newly created segment
        for character in segment:
            #multiply all numbers together within this segment
            #i.e, currentProduct*character, currentProduct*character+1... currentProduct*character+13
            currentProduct = currentProduct * int(character)
            #if this number that has gone through all of the multiplication process is larger than the current number
            if currentProduct > currentNum:
                #set the current number equal to it (aka, the current largest product)
                currentNum = currentProduct

    print(currentNum)
    

biggestProduct(numbers, 13)


   

