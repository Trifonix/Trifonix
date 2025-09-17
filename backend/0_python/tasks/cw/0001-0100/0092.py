## Tribonacci Sequence

# Well met with Fibonacci bigger brother, AKA Tribonacci. As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

def tribonacci(signature, n):
    if n == 2:
        return [signature[0], signature[1]]
    if n == 1:
        return [signature[0]]
    if n == 0:
        return []
    arr = signature
    for x in range(3, n):
        temp = 0
        temp += arr[-1] + arr[-2] + arr[-3]
        arr.append(temp)
    return arr
