import random								
A = [5,3,8,6,1,9,2,7]									


def shuffle(array):										
    arraylen = len(array)								
    if len(array) < 2:
    	print("Too short")

    for index in range (arraylen):						
        swap = random.randrange(arraylen-1)				
        swap += swap >= index                           
        array[index], array [swap] = array[swap], array[index]  

shuffle(A) 
print (A) 
#The big O notation for Question one would be O(n).
#This is because the longer the array the longer the runtime 
#This means that the time it would take to execute linearly increases.



import math
def zeros_in_factorial(n):

    if n < 5:
        print ("0")

    count = 0
    i = 5
    while n//i >= 1:
        count += n // i
        i *= 5
    return count
    print (count)

i = 0

def factorials (i):
    anw = math.factorial(i)
    return anw

i = int(input("Enter a number "))
print ("The Factorials are : ",factorials(i))
print ("Number of Trailing zeros ",zeros_in_factorial(i))
#The big O notation for Question one would be O(n).
#This is because there is a loop which depends on a number the user inputs
#The smaller the number the shorter the calculations will be, the longer, 
#the more calculations would be. The time it take to execute linearly increases