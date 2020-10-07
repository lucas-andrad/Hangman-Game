from words import words
import random

def selectWord():
    word = random.choice(words)
    return word.upper()

def play(word):
    word_length = "_" * len(word)
    correct_word = False
    used_letters = []
    used_words = []
    guesses = 9

    print("Let's play!")
    print(showHangman(guesses))
    print('This is the word: ' + word_length)
    print(word)
    while not correct_word and guesses > 0:
        guess = input('Type a word or letter to continue: ').upper()
        if len(guess) == 1 and guess.isalpha():
            print(guess)
            if guess in used_letters:
                print('You already used this letter. Try again')
            elif guess not in word:
                print('You missed.')
                guesses = guesses - 1
                used_letters.append(guess)
            else:
                print('Correct letter!')
                used_letters.append(guess)
                word_list = list(word_length)
                index = [i for i, letter in enumerate(word) if letter == guess]
                for i in index:
                    word_list[i] = guess
                word_length = ''.join(word_list)
                if "_" not in word_length:
                    correct_word = True
        else:
            print("Invalid guess. Try again")
        print(word_length)




def showHangman(guess): 
    states = ['''   _______
                    |/      |
                    |       0
                    |      /|\\
                    |       |
                    |    _/  \\_ 
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |      /|\\
                    |       |
                    |      / \\_ 
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |      /|\\
                    |       |
                    |      / \\
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |      /|\\
                    |       |
                    |        \\
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |      /|\\
                    |       |
                    |
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |       |\\
                    |       |
                    |
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |       |
                    |       |
                    |
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |       |
                    |
                    |
                    |
                    |___''','''
                    _______
                    |/      |
                    |       0
                    |
                    |
                    |
                    |
                    |___''','''
                    _______
                    |/      |
                    |
                    |
                    |
                    |
                    |
                    |___''']
    return states[guess]

def init():
    word = selectWord()
    play(word)

init()
