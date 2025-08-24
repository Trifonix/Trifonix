## Credit Card Mask

# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it. Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    new_str = ""
    for i in range(len(cc)):
        if i < len(cc) - 4:
            new_str += "#"
        else:
            new_str += cc[i]
    return new_str
