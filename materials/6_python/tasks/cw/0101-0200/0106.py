## Human Readable Time

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

"""
def make_readable(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    seconds %= 60

    s = str(seconds)
    if len(s) == 1:
        s = '0' + s

    m = str(m)
    if len(m) == 1:
        m = '0' + m

    h = str(h)
    if len(h) == 1:
        h = '0' + h

    return f"{h}:{m}:{s}"
"""

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    print(hours, seconds)
    minutes, seconds = divmod(seconds, 60)
    print(minutes, seconds)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
