## Fake Binary

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(str):
    str = list(str)
    for i in range(len(str)):
        if str[i] < '5':
            str[i] = '0'
        elif str[i] > '4':
            str[i] = '1'
    return ''.join(str)
