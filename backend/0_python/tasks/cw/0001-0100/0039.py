## Shortest Word

# Simple, given a string of words, return the length of the shortest word(s). String will never be empty and you do not need to account for different data types.

def find_short(s):
    shortest_word = ""
    current_word = ""
    for ch in s:
        if ch != " ":
            current_word += ch
        else:
            if shortest_word == "" or len(current_word) <= len(shortest_word):
                shortest_word = current_word
            current_word = ""
    if shortest_word == "" or len(current_word) < len(shortest_word):
        shortest_word = current_word
    return len(shortest_word)
