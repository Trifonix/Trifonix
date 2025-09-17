# RGB To Hex Conversion

## The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value. Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

"""
def int_to_hex(n):
    res = hex(n)[2:].upper()
    if 0 <= n <= 15:
        return '0' + res
    elif n < 0: return "00"
    elif n > 255: return "FF"
    else: return res
def rgb(r, g, b):
    return int_to_hex(r) + int_to_hex(g) + int_to_hex(b)
"""

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
