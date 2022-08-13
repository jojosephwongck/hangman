import random

f = open("HangmanDatabase.txt", "r")
DataBase = f.read()
WordList = DataBase.split(",")
f.close()
index = random.randint(0, len(WordList) - 1)
ans = WordList[index]

k = len(ans)
display = '_'*k
AllLetter = 'abcdefghijklmnopqrstuvwxyz'
CorrectLetter = ''
TrialCount = 6
EndGame = False
Used = ''
HangPic = ['''
=======|
       |
       |
       |
''',
'''
=======|
   O   |
       |
       |
''',
'''
=======|
   O   |
   |   |
       |
''',
'''
=======|
   O   |
  /|   |
       |
''',
'''
=======|
   O   |
  /|\  |
       |
''',
'''
=======|
   O   |
  /|\  |
  /    |
''',
'''
=======|
   O   |
  /|\  |
  / \  |
''']

def InputGuess():
    global Used
    guess = input('Guess a letter: ')
    if guess not in AllLetter or len(guess) != 1:
        print('Please enter a valid letter.')
    elif guess in Used:
        print('Try another unused letter.')
    else:
        Used += guess
        return guess

while not EndGame :
    guess = InputGuess()
    if guess:
        if guess in ans:
            CorrectLetter += guess
        else:
            TrialCount -=1

        for i in range(k):
            if ans[i] in CorrectLetter:
                display = display[:i] + ans[i] + display[i + 1:]

        print('The word guessed is: \n' + display)
        print(HangPic[6 - TrialCount])
        print('Number of trials left: ' + str(TrialCount))
        print('Used letter(s): ' + Used)

        if TrialCount == 0 or display == ans:
            EndGame = True

if display == ans:
    print('You are smart! The answer is ' + ans + '.')
else:
    print('Sorry, you lose:/')
    print('The answer is : ' + ans)