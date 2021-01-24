import datetime

def main():
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
			           'hard text3' : 'Text text. Text. Text, text. Text?' 
				                  'Text!'}
			}

	while True:
		difficulty = chooseDiff()
		choice = chooseText(texts, difficulty)
		text = texts[difficulty][choice]
		print(f'Your text:\n{text}')
		text = insertNewLine(text)
		text = text.split('\n')
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
	totalErrors = 0
	for s in text:
		print(s)
		inpt = input()
		errors = countErrors(s, inpt)
		totalErrors += errors

	return totalErrors


def countErrors(sentence, inpt):
	errors = 0
	inpt = inpt.split()
	for w in inpt:
		if w not in sentence:
			errors += 1

	return errors


def calcWpm(text, test, time):
	time = time.total_seconds() / 60
	words = text.split()
	nWords = len(words)
	wpm = round(nWords / time)

	return wpm


def makeAccu(text, test):
	accuracy = ((len(text) - test) / len(text)) * 100

	return accuracy


def evaluation(wpm, accuracy):
	print(f'Your typing speed is {wpm} wpm with {accuracy}% accuracy!')


def insertNewLine(text):
	newText = ''
	last = ''
	for i in text:
		if last == '.' or last == '?' or last == '!':
			i = '\n'
		newText += i
		last = i

	return newText


main()
