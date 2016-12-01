def highestPerfectSquare(n):
    x = n                                                       # x is equal to n
    while True:												
        if x**2 <=n:									        # if x**2 is less than or equal to n
            print("The highest perfect square is " + str(x**2)) # print "comment" and x 
            return x**2										
        else:				
            x-=1												# x minus 1 and set it		
highestPerfectSquare(int(input("Enter a number ")))             #Value of n

#Pseudo Code
# highestPerfectSquare(n)
# x←n
# 	while True
# 		IF x**2 <=n
# 			PRINT("The highest perfect square is" + str(√x))
# 			RETURN str(√x)
# 		ELSE 
# 		 	x-1