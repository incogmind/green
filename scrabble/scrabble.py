#scrabble problem

import sys

def findWords(givenScores,givenListofWords,givenRackofLetters):
	valid_words=[]
	valid_score=[]

	for word in givenListofWords:

		temprackofLetters= list(givenRackofLetters)
		score=0
		for index,letter in enumerate(word):
			#print temprackofLetters
			if temprackofLetters==[""]:
				break
			elif letter in temprackofLetters:
				if len(temprackofLetters)==1:
					temprackofLetters=[""]
				else:
					temprackofLetters.remove(letter)
					
				score+=int(givenScores[letter])
			else:
				break
			if index==len(word)-1:
				valid_words.append(word)
				valid_score.append(score)
	return valid_words,valid_score



def main(argv):

#given Scores
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
	listofWords=[]
	#take file input for thr sowpods file
	fileInput=open(argv[1])
	
	#populate the listofWords

	for line in fileInput:
		listofWords.append(line.strip().lower())

	if not argv[2]:
		exit()

	rackofLetters=argv[2].lower()

	resWords,resScores=findWords(scores,listofWords,rackofLetters)
	for index,words in enumerate(resWords):
		print words +" "+str(resScores[index])


	

if __name__ == '__main__':
	main(sys.argv)