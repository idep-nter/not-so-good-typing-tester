import datetime

def main():
    """
    The main function prints an intro and asks the user to enter a difficulty 
    and to choose a specific text. When he is ready, timer starts and he is 
    trying to type every sentece one by one.  
    At the end it prints evaluation and asks user he wants to repeat the test.
    """
    intro()
    texts = {'easy' : {'easy text1' : 'Text text. Text.',
                       'easy text2' : 'Text text. Text.',
                       'easy text3' : 'Text text. Text.'},

             'medium' : {'medium text1' : 'Text text. Text. Text, text.',
                         'medium text2' : 'Text text. Text, text.',
                        'medium text3' : 'Text text. Text. Text, text.'},

             'hard' : {'hard text1' : 'Text text. Text. Text, text. Text?' 
                                      ' Text!',  
                       'hard text2' : 'Text text. Text. Text, text. Text?'  
                                      ' Text!',
                       'hard text3' : 'Text text. Text. Text, text. Text?' 
                                      ' Text!'}
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
    Asks the user to choose a difficulty and checks the answer.
    """
    while True:
        try:
            difficulties = ['easy', 'medium', 'hard']
            difficulty = input('Choose difficulty: easy / medium / hard\n')
            if difficulty.lower() not in difficulties:
                raise ValueError
        except ValueError:
            print('Please select correct difficulty.')
            continue
        else:
            break

    return difficulty

def chooseText(texts, difficulty):
    """
    Asks the user to choose a text from previously selected difficulty and 
    checks the answer.
    """
    while True:
        try:
            names = list(texts[difficulty].keys())
            print(names)
            text = input('Choose text: ')
            if text not in names:
                raise ValueError
        except ValueError:
            print('Please type a correct name of the choosen text.')
            continue
        else:
            break

    return text

def textType(text):
    """
    Inserts a new line character after every sentence and splits the text by it. 
    After that it prints sentence one by one and asks the user to write it. 
    After each iteration it checks the sentence for errors. 
    At last function returns the total number of them.
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

def countErrors(sentence, inpt):
    """
    Counts errors in the sentence by iterating throught it and checking if a 
    words exists in the original one.
    """
    errors = 0
    inpt = inpt.split()
    for w in inpt:
        if w not in sentence:
            errors += 1

    return errors

def calcWpm(text, test, time):
    """
    Calculates word per minute by spliting time into minutes and dividing it
    with number of words in the text.
    """
    time = time.total_seconds() / 60
    words = text.split()
    nWords = len(words)
    wpm = round(nWords / time)

    return wpm


def makeAccu(text, test):
    """
    Makes user's accuracy by calculating number of correct words in the text,
    dividing it with total number of words and multipling the remainder with 100
    at the end.
    """
    words = text.split()
    accuracy = ((len(words) - test) / len(words)) * 100

    return accuracy

def evaluation(wpm, accuracy):
    """
    Simply prints user's wpm and accuracy.
    """
    print(f'Your typing speed is {wpm} wpm with {accuracy}% accuracy!')

def insertNewLine(text):
    """
    Inserts a new line char after every sentence and returns the modified text.
    """
    newText = ''
    last = ''
    for i in text:
        if last == '.' or last == '?' or last == '!':
            i = '\n'
        newText += i
        last = i

    return newText

main()
