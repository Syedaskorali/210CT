import random											#imports random
A = [5,3,8,6,1,9,2,7]									#Array with the values


def shuffle(array):										#function with value array
    arraylen = len(array)								#arraylen = length of array
    if len(array) < 2:									#If the length of array < 2 do the following
    	print("Too short")								#print too short

    for index in range (arraylen):						#for all the indexes in arraylen
        swap = random.randrange(arraylen-1)				#swap = random number in the range -1 because of 0 being an index too
        swap += swap >= index                           
        array[index], array [swap] = array[swap], array[index]  #swaps the two indexes

shuffle(A) #Give array the value of A and runs the function
print (A) #prints the array
