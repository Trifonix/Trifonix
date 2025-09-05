## Mumbling

# This time no story, no theory. The examples below show you how to write function accum:

def accum(st):
    str = ""
    for x in range(len(st)):
        str += st[x].upper()
        for _ in range(x):
            str += st[x].lower()
        if x != len(st)-1:
            str += '-'
    return str
