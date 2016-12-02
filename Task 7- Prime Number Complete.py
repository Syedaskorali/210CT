#Write a recursive function (pseudocode and code) to check if a number n is prime (hint: check whether
#n is divisible by any number below n)

#1 2 3 5 7 11 13
#Function that can check if the number can be divided by any number below itself except 1
#use count down for the recursion.
#Variables n = the number  ans = final answer x = n-1



def primenumbercheck():
    nstring = input(("Enter a number "))
    PrimeOrNotPrime = 0
    n = int(nstring)
    x = n-1

    while x > 1:
        if n%x==0:
            print ("Not Prime")
            PrimeOrNotPrime = PrimeOrNotPrime + 1
        else:
            print("Prime")
            
        x = x - 1



    if PrimeOrNotPrime > 0:
        print ("The Answer for the value is: NOT PRIME")
    else: 
        print ("The Answer for the value is: PRIME")
    
primenumbercheck()

#PsuedoCode
#primenumbercheck()
#nstring←input
#PrimeOrNotPrime←0
#n←int(nstring)
#x←n-1
#while x >1
    #if n%x←1
    #primeornotprime ←prieornotprime+1
    #else x=x_!

# nstring is the value of n but in string format so user
#can input whilst we ask a question which is then used by variable n
# x is n-1 since we cant divide n by itself so we always start one
#number below. while x >1 it does n%x making sure there are no remainder
#if there were remainders then that would mean the number is prime
#we have to recursively do n%x till x is 1. if n%x ==0 at any time
#PrimeOrNotPrime will be PrimeOrNotPrime = PrimeOrNotPrime +1
#this will then be used in the if statement if PrimeOrNotPrime >0 meaning
#the not prime statement was triggered at least once meaning the overall
#value is not prime. For a number to be prime it must always meet the
#prime statement.
