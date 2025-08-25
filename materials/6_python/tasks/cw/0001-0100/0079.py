## Your order, please

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result. Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(sentence):
  res = sentence.split()
  arr = res.copy()
  i = 0
  for x in res:
    for y in x:
      y = ord(y)
      if y >= ord("0") and y <= ord(":"):
        i = int(chr(y))-1
    arr[i] = x
    i += 1
  return " ".join(arr)
