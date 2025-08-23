## Create Phone Number

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(numbers):
    ph_str = ""
    for i, num in enumerate(numbers):
        if i == 0:
            ph_str += "("
        elif i == 3:
            ph_str += ") "
        elif i == 6:
            ph_str += "-"
        ph_str += str(num)
    return ph_str
