## Stop gninnipS My sdroW!

# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    arr = sentence.split()
    good_sentence = ""
    for word in arr:
        if len(word) >= 5:
            good_sentence += word[::-1] + " "
        else:
            good_sentence += word + " "
    return good_sentence.strip()
