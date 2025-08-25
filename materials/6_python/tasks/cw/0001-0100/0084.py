## Simple Pig Latin

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def func(x):
    for l in x.lower():
        if ord(l) in range(ord('a'), ord('{')):
            return True
        
def pig_it(text):
    return " ".join([(x[1:] + x[0]+"ay") if func(x) else x for x in text.split()])
