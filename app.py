from words import words
import random

def selectWord():
    word = random.choice(words)
    return word.upper()

