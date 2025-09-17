## Abbreviate a Two Word Name

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them. The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    newName = ''
    for i in range(len(name)):
        if i == 0:
            newName += name[i].upper()
        elif name[i] == ' ':
            newName += '.'
            newName += name[i + 1].upper()
    return newName
