import datetime

def main():
	"""
	Main function prints intro and asks to choose difficulty and the text. 
	Prints the whole text and when is user ready it starts timer. 
	Each sentence is printed alone so user won't get lost in the longer texts.
	After all is done, program calculates user's wpm and accuracy and prints it.
	At the end it asks user if he want's to try again.
	"""
	intro()
	texts = {'easy' : {'easy text1' : 'Text text. Text.',
					   'easy text2' : 'Text text. Text.',
					   'easy text3' : 'Text text. Text.'},

			 'medium' : {'medium text1' : 'Text text. Text. Text, text.',
			 			 'medium text2' : 'Text text. Text, text.',
			 			 'medium text3' : 'Text text. Text. Text, text.'},

			 'hard' : {'hard text1' : 'Text text. Text. Text, text. Text?' 
			 						  'Text!',  
			 		   'hard text2' : 'Text text. Text. Text, text. Text?' 
			                          'Text!',
			 		   'hard text3' : 'Text text. Text. Text, text. Text? Text!'
			 		   }
			}

	while True:
		difficulty = chooseDiff()
		choice = chooseText(texts, difficulty)
		text = texts[difficulty][choice]
		print(f'Your text:\n{text}')
		input('Press enter when you are ready.')
		start = datetime.datetime.now()
		test = textType(text)
		end = datetime.datetime.now()
		time = end - start
		wpm = calcWpm(text, test, time)
		accuracy = makeAccu(text, test)
		print(f'Your typing speed is {wpm} wpm with {accuracy}% accuracy!')
		again = input('Want to try again? ')
		if again.lower() == 'y' or again.lower() == 'yes':
			continue
		else:
			exit()


def intro():
	print("""
Hello! This a typing tester - an application where you can test how good you are
 in typing! 

You will be shown few texts from which you will be able choose one.

After that you will try to type the text as soon as possible with least mistakes
 as you can!

Happy typing!

	""")


def chooseDiff():
	"""
	Asks user to select a difficulty and checks the answer.
	"""
	while True:
		try:
			difficulties = ['easy', 'medium', 'hard']
			difficulty = input('Choose difficulty: easy / medium / hard\n')
			if difficulty.lower() not in difficulties:
				raise ValueError
			else:
				break

		except ValueError:
			print('Please select correct difficulty.')
			continue

	return difficulty


def chooseText(texts, difficulty):
	"""
	Asks user to selected a text from previously chosen diffulty and checks the
	answer.
	"""
	while True:
		try:
			names = list(texts[difficulty].keys())
			print(names)
			text = input('Choose text: ')
			if text not in names:
				raise ValueError
			else:
				break

		except ValueError:
			print('Please type a correct name of the choosen text.')
			continue

	return text


def textType(text):
	"""
	Inserts new line after each sentence and splits the text by it. Ten prints 
	each sentence, asks user to write it and checks for errors. Returns total
	number of errors.
	"""
	totalErrors = 0
	text = insertNewLine(text)
	text = text.split('\n')
	for s in text:
		print(s)
		inpt = input()
		errors = countErrors(s, inpt)
		totalErrors += errors

	return totalErrors


def insertNewLine(text):
	"""
	Inserts new line character after every sentence and returns modified text.
	"""
	newText = ''
	last = ''
	for i in text:
		if last == '.' or last == '?' or last == '!':
			i = '\n'
		newText += i
		last = i

	return newText



def countErrors(sentence, inpt):
	"""
	Simply checks correctness of each word in user's sentence by checking the 
	original one. Returns number of errors.
	"""
	errors = 0
	inpt = inpt.split()
	for w in inpt:
		if w not in sentence:
			errors += 1

	return errors


def calcWpm(text, test, time):
	"""
	Calculates words per minute by spliting correct time in minutes and dividing 
	it with number of words in text.
	"""
	time = time.total_seconds() / 60
	words = text.split()
	nWords = len(words)
	wpm = round(nWords / time)

	return wpm


def makeAccu(text, test):
	"""
	Makes user's accuracy by calculating number of correct words divided by
	total number of words in the text and multiply it by 100 at the end.
	"""
	words = text.split()
	accuracy = ((len(words) - test) / len(words)) * 100

	return accuracy


def evaluation(wpm, accuracy):
	"""
	Print evalution of user with his wpm and accuracy.
	"""
	print(f'Your typing speed is {wpm} wpm with {accuracy}% accuracy!')


main()
