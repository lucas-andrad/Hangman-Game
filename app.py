from words import words
import random

def selectWord():
    word = random.choice(words)
    return word.upper()

def play(word):
    word_length = "_ " * len(word)
    correct_word = False
    used_letters = []
    used_words = []
    guesses = 9

    print("Let's play!")
    print(showHangman(guesses))
    print('This is the word: ' + word_length)


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
