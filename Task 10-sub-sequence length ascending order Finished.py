originalArray =[1,2,3,1,2,3,4,1,2,3,4,5,10,1,2,3,4,5,6,7,8]

subsequence=[]
longestSubsequence=[]
finalSubsequence=longestSubsequence
def sequence_checker(array,x):
	global subsequence                                              #Calling subsequence
	global longestSubsequence                                       #Calling longestSubsequence
	count = len(originalArray)										#Count is the length of original array

	
	while count > 0:                               					#while count is greater then 0 do the following
		if x==0:													#if x is equal to 0
			subsequence.append(array[x])							#add the value of position 0 into subsequence
			x=x+1													# adds 1 to x
			count=count-1											#subtracts 1 from count

		elif array[x] > subsequence[-1]:							#else if the position x in array(originalarray) is greater that the last position in subsequence
			subsequence.append(array[x])							##add the value of position x in array into subsequence
			x=x+1													#adds 1 to x
			count=count-1											#subtracts 1 from count

		else:														#else
			longestSubsequence.append(subsequence[:])             	#longsubsequence adds subsequence to its array by making another array inside the array with the sequence e.g.[[123][1234]]				
			del subsequence[:]										#deletes previous subsequence
			subsequence.append(array[x])							#add the value of position x in array into subsequence
			x=x+1													#adds 1 to x
			count=count-1											#subtracts 1 from count
	
	longestSubsequence.append(subsequence)							#adds the last sequence in subsequence to longestsubsequence as its out the while loop, which is why is indented out.
	#print (longestSubsequence)					
sequence_checker(originalArray,0)									#values of sequence checker the array and x is given value of 0 to start with



def length(finalSubsequence,y):										#New function to check the length of each array in finalsubsequence (which holds the array from longestsubsequence)

	while len(finalSubsequence) > 1:								#while the length of finalsubsequence is greater than 1 do the following
																	#Note keep in mind finalsubsequence is an array which is holding arrays #nested
		if len(finalSubsequence[y]) < len(finalSubsequence[-1]):	#if the length of pos y in finalsubsequence is less than the length of the last value in last finalsubsequence	
			del finalSubsequence[y]									#delete value in pos y in finalsubsequence
			

		elif len(finalSubsequence[y]) > len(finalSubsequence[-1]):  #else if the length of pos y in finalsubsequence is greater than the length of the last value in last finalsubsequence
			del finalSubsequence[-1]								# delete value in pos last in finalsubsequence(pos last = last position in finalsubsequence).
		else:														#Else
			return("Error")											#Return Error, for my use to see if program was running as it should
			

	print(finalSubsequence[0])										#print finalsubsequence position 0 since its an array with in an array you can do it without pos, will still work fine but will show extra layer of square bracket
length(finalSubsequence,0)											#function values.












