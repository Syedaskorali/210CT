def vocalreduction (word):
	illegalLetters = ["a", "e", "i", "o", "u"]

	if len(word)<=1:#If word is 1 or less than one print out the word or should i say letter
		return word	

	elif any(char in illegalLetters for char in word[0]):#character from illegal letters matches character in word pos 0
		return vocalreduction (word[1:])#slice starting at next letter of word		
	else:
		return word[0] + vocalreduction(word[1:])#if theres no illegal letters dont delete, just carry on to next pos
print(vocalreduction(str(input("input a word "))))
