array = [2,3,5,7,9,13]                              # The array and the values of the array
array = sorted(array)                               # Sorts the array into order of low to high
x= int(input("Enter a low number "))                # x = the low number   
y= int(input("Enter a high number "))               # y = the high number  
modifiedArray= array                                # modifiedArray is another array with the values of array

def binarySearch(numArray, key):                    #Binary Search Function
    low = 0
    high = len(numArray)-1
    found = False

    while low<=high and not found:
        middle = (low + high)//2
        if numArray[middle] == key:
            return True

        else:
            if key < numArray[middle]:
                high = middle-1
                
                
            elif key > numArray[middle]:
                low = middle+1
            else:
                return true  
    if found is not True:                           #If the number has not been found
        modifiedArray.append(key)                   #add it to the modifiedarray


binarySearch(array, x)                              #do function binarysearch using the values of array and x
binarySearch(array, y)                              #do function binarysearch using the values of array and x

def my_search(array,lo,hi):     
    interval=[]                 #stores the the intervals
    for i in modifiedArray:                #numbers in the array
        if (i> lo and i <hi):   # if numbers in modifiedarray are greater than low and less than high
            interval.append(i)
            # print("Number in interval are: ",interval) For development testing
                                # interval.append the numbers in the interval
    if not interval:                  # checks if anything is in interval
        return False            # if there is nothing in interval return false
    else:                       #else (this means values have been added to the list meaning there were values found within the interval)
        return True             #Return true, meaning there are value in interval

print (my_search(array,x,y))    #print array, input value x which is lo and y which is high.

















#               # number to search for
# array = [2,3,5,7,9,13]
# array = sorted(array)       # sorted() returns a new list

# print(array)          # show us what you've got
 
# #    Search for number in array
# def binary_search(number, array, lo, hi):
 
#     if hi < lo: return -1       # no more numbers
#     mid = (lo + hi) // 2        # midpoint in array
#     if number == array[mid]:
#         return mid                  # number found here
#     elif number < array[mid]:
#         return binary_search(number, array, lo, mid - 1)     # try left of here
#     else:
#         return binary_search(number, array, mid + 1, hi)     # try above here
 
# def my_search(array,lo,hi):     # convenience interface to binary_search()
#     a2=[]                       #list 2, one that stores the the intervals
#     for i in array:             #numbers in the array
#         if (i> lo and i <hi):   # if numbers in array are greater than low and less than high
#             a2.append(i)        # a2.append the numbers in the interval
#     if not a2:                  # checks if anything is in list 2
#         return False            # if there is nothing in list 2 return false
#     else:                       #else (this means values have been added to the list meaning there were values found within the interval)
#         return True             #Return true, meaning there are value in list 2
   
# print (my_search(array,int(input("Enter the Low number ")),int(input("Enter the high number "))))    #print array, enter low input and high input.