def wordReversal(word):														# function 		
    split_text = word.split(" ")                                            # split_text is the word entered split with " " 
    result = []                                                             # result = list
    for word in range(len(split_text) -1,-1,-1):                            # for words in split text reverse them
        result.append(split_text[word])                                     # Then append split_text[word] into result
    return " ".join(result)		                                            # return result 
x =(input("what would you would like to reverse?" ))                        #
print (wordReversal(x))                                                     #
#Psuedo Code
# WordReversal(word)
# 	split_text←word.split(" ")
# 	result←[]
# 	FOR word in range(len split_text) -1,-1,-1
# 		result.append(split_text[word])
# 		RETURN " ".join(result)

