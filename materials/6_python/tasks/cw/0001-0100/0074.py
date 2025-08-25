## A Needle in the Haystack

# Can you find the needle in the haystack? Write a function findNeedle() that takes an array full of junk but containing one "needle" After your function finds the needle it should return a message (as a string) that says: "found the needle at position " plus the index it found the needle, so.

def find_needle(haystack):
    res = "Your function didn't return anything"
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            res = f"found the needle at position {i}"
            break
    return res
