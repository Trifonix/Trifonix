## Convert number to reversed array of digits

# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    new_arr = []
    while n > 0:
        new_arr.append(n % 10)
        n //= 10
    return [0] if len(new_arr)==0 else new_arr
