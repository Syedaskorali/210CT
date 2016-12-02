import math                                                         #imports maths      

def zeros_in_factorial(n):                                          #function 

    if n < 5:                                                       #if n is less than 5 do the following
        print ("0")                                                 #print 0

    count = 0                                                       # set count to 0
    i = 5                                                           # set i to 5
    while n//i >= 1:                                                # while n divided by i(getting rid of remainder also) is greater or = to 1 do the following
        count += n // i                                             # count = count + n//i
        i *= 5                                                      # i=i*5
    return count                                                    # return count
    print (count)                                   


                                                              




def factorials (i):                                                #gives factiorials       
    anw = math.factorial(i)
    return anw


i = int(input("Enter a number "))
print ("The Factorials are : ",factorials(i))
print ("Number of Trailing zeros ",zeros_in_factorial(i))


