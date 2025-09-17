## String ends with?

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    if len(ending) > len(text):
        return False
    for x in text[::-1]:
        for y in ending[::-1]:
            if x == y:
                ending = ending[:-1]
                if not ending:
                    return True
                break
            else:
                return False
