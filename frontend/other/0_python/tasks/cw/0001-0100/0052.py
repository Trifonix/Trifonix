## Replace With Alphabet Position

# Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    return " ".join([str(ord(letter.lower())-96) for letter in list(text) if ord(letter.lower()) in range(ord("a"), ord("{"))])
