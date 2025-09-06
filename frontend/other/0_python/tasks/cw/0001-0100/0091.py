## Printer Errors

# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

def printer_error(s):
    errors = 0
    for x in s:
        if ord(x) not in range(ord('a'), ord('m')+1):
            errors += 1
    return f"{errors}/{len(s)}"
