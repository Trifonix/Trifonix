## Who likes it?

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

def likes(names):
    count = len(names)
    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {count - 2} others like this"
