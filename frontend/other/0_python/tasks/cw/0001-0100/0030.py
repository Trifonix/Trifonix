## Get the Middle Character

# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string. If the string's length is odd, return the middle character. If the string's length is even, return the middle 2 characters.

def get_middle(s):
    if len(s)%2:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1]+s[len(s)//2]
