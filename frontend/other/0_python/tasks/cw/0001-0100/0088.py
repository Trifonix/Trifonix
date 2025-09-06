## Split Strings

# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

def solution(s):
    if len(s)>1:
        str = ""
        count = 0
        for x in s:
            str += x
            count += 1
            if count==2:
                str += " "
                count = 0
        if str[-2] == " ":
            str += '_'
        return str.strip().split()
    else:
        return [f"{s}_"] if len(s)==1 else []
